'''
@date Jun 27, 2010
@author Matthew A. Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

from . import IParse
from ..TestResults import TestResults, Suite, TestCase, Notice
from TestParser.Common.Constants import Constants
import re



class SuiteHierarchyDict(object):
    '''
    Used to simplify structuring of suites. Uses a tree-hierarchy reminiscient
    of k-ary trees. Basically a custom dictionary based on dictionaries.
    
    @date Jul 20, 2010
    '''
    def __init__(self):
        self.suites = {}

    @staticmethod
    def splitSuite(suite):
        '''
        Takes in the long suite name and breaks it down to be used for
        a suite hierarchy.
        
        suite is something like: mod1.mod2.mod3.class
        '''
        suite = suite.strip("()")
        return suite.split(".")

    def _addSuite(self, suitePath):
        '''
        Adds suite to the dictionary, so that we can later add data.
        
        @date Jul 20, 2010
        '''
        splitSuite = self.splitSuite(suitePath)

        lastSuite = self.suites
        for suite in splitSuite:
            if suite not in lastSuite:
                lastSuite[suite] = {}

            lastSuite = lastSuite[suite]

    def addData(self, suitePath, name, status=None, file=None, line=None, info=None):
        '''
        Add data to our 'dictionary'.
        
        suitePath is something to the effect of: 'mod1.mod2.mod3.class' the
        data is stored like so: dict[mod1][mod2][mod3][class] = data

        @date Jul 20, 2010
        '''
        self._addSuite(suitePath)

        splitSuite = self.splitSuite(suitePath)

        lastSuite = self.suites
        for suite in splitSuite:
            lastSuite = lastSuite[suite]

        if name not in lastSuite:
            lastSuite[name] = TestData()

        lastSuite[name].name = name
        if status is not None:
            lastSuite[name].status = status
        if file is not None:
            file = file.strip(',')
            file = file.strip('"')
            lastSuite[name].file = file
        if line is not None:
            line = line.strip(',')
            lastSuite[name].line = int(line)
        if info is not None:
            lastSuite[name].info = info

class TestData(object):
    '''
    represents all the data we can collect on a test.
    
    @date Jul 20, 2010 
    '''
    def __init__(self):
        self.name = None
        self.status = None
        self.file = None
        self.line = None
        self.info = None

    def __str__(self):
        return "TestData(%s, %s, %s, %s, %s)" % \
            (self.name, self.status, self.file, self.line, self.info)

    def __repr__(self):
        return self.__str__()



class PythonUnittestParser(IParse.IParse):
    '''
    Parser for Python's unittest framework
    
    The following is example output from a pyhton unittest runner.
    (1) are lines to be validated by _validStatusLine()
    (2) are lines to be validated by _validFailLine()
    (3) are lines to be validated by _validFailInfoLine()
    
    @verbatim
    test_choice (__main__.TestSequenceFunctions) ... ok                    (1)
    test_error (__main__.TestSequenceFunctions) ... ERROR                  (1)
    test_fail (__main__.TestSequenceFunctions) ... FAIL                    (1)
    test_sample (__main__.TestSequenceFunctions) ... ok                    (1)
    test_shuffle (__main__.TestSequenceFunctions) ... ok                   (1)
    
    ======================================================================
    ERROR: test_error (__main__.TestSequenceFunctions)                     (2)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "python_unittest_example.py", line 43, in test_error            (3)
        raise NotImplementedError
    NotImplementedError
    
    ======================================================================
    FAIL: test_fail (__main__.TestSequenceFunctions)                       (2)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "python_unittest_example.py", line 40, in test_fail             (3)
        self.fail()
    AssertionError: None
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s
    
    FAILED (failures=1, errors=1)
    @endverbatim
    
    
    @warning This only works if the data is output correctly. 
    @see TestParser.Model.PythonUnittestRunner
    
    @date Jun 27, 2010
    @author Matthew A. Todd
    '''

    VALID_STATUS_LINE_REGEX = r'^[a-zA-z0-9_]+'     \
                            ' \([a-zA-z0-9_.]+\)'   \
                            ' \.{3}'                \
                            ' (FAIL|ERROR|ok)$'           # name (suite) ... status           
    VALID_FAIL_LINE_REGEX = r'^(FAIL|ERROR):'               \
                            ' [a-zA-z0-9_]+'        \
                            ' \([a-zA-z0-9_.]+\)$'  # FAIL: name (suite)
                                                    # ERROR: name (suite)
    VALID_FAIL_INFO_LINE_REGEX = r'^  File'         \
                            ' "[a-zA-z0-9_/]+\.[a-zA-z0-9]+",' \
                            ' line [0-9]+,'         \
                            ' in [a-zA-z0-9_]+$'    #   File "filename.ext", line num, in name

    def __init__(self):
        '''
        Constructor
        '''
        self.suiteDict = SuiteHierarchyDict()       # stores all test/suite information

        self.validStatusLineRegex = re.compile(PythonUnittestParser.VALID_STATUS_LINE_REGEX)
        self.validFailLineRegex = re.compile(PythonUnittestParser.VALID_FAIL_LINE_REGEX)
        self.validFailInfoLineRegex = re.compile(PythonUnittestParser.VALID_FAIL_INFO_LINE_REGEX)

    def parse(self, file=None, stringData=None):
        '''
        Parse data.
        
        @see IParser.parse()
        '''
        if stringData is not None:
            self._parseData(stringData)
        elif file is not None:
            self._parseData(file.read())
        else:
            #TODO: raise?
            Constants.logger.error("ERROR: parse() needs data to parse")
            return None


        return self._compileTestResults()

    def _parseData(self, stringData):
        '''
        Parses the given string data and sets it up in self.suites
        for later compiling. Gathers information from FAIL tests
        section and stores it in self.failSuites for later use.
        
        
        @param stringData all the data contained w/in a string
        '''
        lines = stringData.split('\n')

        lastFailSuiteName = None
        lastFileName = None
        lastLineNum = None
        lastTestName = None
        lineCount = 0
        lineEncountered = False

        for line in lines:
            if self._validStatusLine(line):
                words = line.split(' ')
                name = words[0]
                suite = words[1]
                status = words[3]

                self.suiteDict.addData(suite, name, status)

            # scraping FAIL messages
            else:
                if self._validFailLine(line):
                    words = line.split(' ')
                    lastFailSuiteName = words[2]

                elif self._validFailInfoLine(line):
                    line = line.strip(' ')
                    words = line.split(' ')
                    lastFileName = words[1]
                    lastLineNum = words[3]
                    lastTestName = words[5]

                    lineCount = 0
                    lineEncountered = True
                elif lineCount == 2 and lineEncountered:
                    info = line
                    self.suiteDict.addData(lastFailSuiteName, lastTestName, file=lastFileName, line=lastLineNum, info=info)

                    lineEncountered = False

                lineCount += 1



    def _compileTestResults(self):
        '''
        Takes the data contained in self.suites and puts it in TestResults
        for returning.
        '''
        results = TestResults.TestResults()

        # TODO: clean up
        for suite in self.suiteDict.suites:
            results.suites.append(self._compileSuite(suite, self.suiteDict.suites[suite]))
        return results

    def _compileSuite(self, name, suite):
        '''
        compiles suites.
        
        Recursive function. Basecase is TestCase, which is signified by
        a non-dict item, hence the try/except.
        
        TODO: change away from try/except if possible
        
        @date Jul 20, 2010
        '''
        if self._isSuite(suite):
            resultSuite = Suite.Suite(name)
            for suiteName in suite.keys():
                resultSuite.testCases.append(self._compileSuite(suiteName, suite[suiteName]))
            return resultSuite
        else:
            return self._compileTestCase(suite)

    def _isSuite(self, suite):
        '''
        Checks to see if its a suite. Suites are stored in a dictionary and
        we're going to be using keys(), so just check if we have that.
        
        @date Jul 20, 2010
        '''
        try:
            suite.keys()
            return True
        except AttributeError:
            return False

    def _compileTestCase(self, data):
        '''
        make a TestCase with the given data
        
        Fail info will only be valid when status is 'FAIL' or 'ERROR', so we can just
        pass in explicit None's for 'ok'.
        
        @date Jul 20, 2010
        '''
        name = data.name
        status = data.status
        file = data.file
        line = data.line
        info = data.info

        resultTest = TestCase.TestCase(name)
        resultTest.addNotice(Notice.Notice(file, line, info, status.lower()))

        return resultTest


    def _validStatusLine(self, line):
        '''
        Uses regex to validate that the given line contains data to extract.
        For use on the one-liner status lines that appear at the beginning
        of python unittest's output.
        
        Line should be of the form:
        
        @verbatim
        name (suite) ... status
        @endverbatim
        
        @see PythonUnittestParser (example)
        
        @param line line to check
        @return true if line is valid
        @date Jun 29, 2010 
        '''
        return self.validStatusLineRegex.match(line) is not None

    def _validFailLine(self, line):
        '''
        Uses regex to validate that the given line is a 'fail line,' by which
        I mean it is the title of a test failure section.
        
        Line should be of the form:
        
        @verbatim
        FAIL: name (suite)
        @endverbatim
        
        @see PythonUnittestParser (example)
        
        @return true if line valid
        @date Jun 29, 2010
        '''
        return self.validFailLineRegex.match(line) is not None

    def _validFailInfoLine(self, line):
        '''
        Uses regex to validate that the given line contains info on a failed
        test case.
        
        Line should be of the form:
        
        @verbatim
          File "filename", line ##, in name
        @endverbatim
        
        Note that there are spaces at the beginning of the line.
        
        @see PythonUnittestParser (example)
        
        @return true if line valid
        @date Jun 29, 2010
        '''
        return self.validFailInfoLineRegex.match(line) is not None
