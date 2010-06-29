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

import sys

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
    
    @date Jun 27, 2010
    @author Matthew A. Todd
    '''
    
    VALID_STATUS_LINE_REGEX = r'^[a-zA-z0-9_]+'     \
                            ' \([a-zA-z0-9_.]+\)'   \
                            ' \.{3}'                \
                            ' (FAIL|ok)$'           # name (suite) ... status           
    VALID_FAIL_LINE_REGEX = r'^FAIL:'               \
                            ' [a-zA-z0-9_]+'        \
                            ' \([a-zA-z0-9_.]+\)$'  # FAIL: name (suite)
    VALID_FAIL_INFO_LINE_REGEX = r'^  File'         \
                            ' "[a-zA-z0-9_/]+\.[a-zA-z0-9]+",' \
                            ' line [0-9]+,'         \
                            ' in [a-zA-z0-9_]+$'    #   File "filename.ext", line num, in name

    def __init__(self):
        '''
        Constructor
        '''
        self.suites = {}        # contains dictionary of suites -> test statuses: (name, status)
        self.failSuites = {}    # contains dictionary of suites -> failed tests-> failure info: (file, line)
    
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
            #TODO: raise
            Constants.logger.error("ERROR: parse() needs data to parse")
            return
            
            
        return self._compileTestResults()
    
    def _parseData(self, stringData):
        '''
        Parses the given string data and sets it up in self.suites
        for later compiling. Gathers information from FAIL tests
        section and stores it in sef.failSuites for later use.
        
        
        @param stringData all the data contained w/in a string
        '''
        lines = stringData.split('\n')
        
        lastFailSuiteName = None
        
        for line in lines:
            if self._validStatusLine(line):
                words = line.split(' ')
                name = words[0]
                suite = words[1]
                status = words[3]
                
                if suite not in self.suites:
                    self.suites[suite] = []
                    
                self.suites[suite].append((name, status))
                
            # scraping FAIL messages
            else:
                if self._validFailLine(line):
                    words = line.split(' ')
                    lastFailSuiteName = words[2]
                    
                elif self._validFailInfoLine(line):
                    line = line.strip(' ')
                    words = line.split(' ')
                    file = words[1]
                    line = words[3]
                    test = words[5]
                    
                    if lastFailSuiteName not in self.failSuites:
                        self.failSuites[lastFailSuiteName] = {}
                    
                    self.failSuites[lastFailSuiteName][test] = (file, line)
                    
                    
            
    def _compileTestResults(self):
        '''
        Takes the data contained in self.suites and puts it in TestResults
        for returning.
        
        Fail info will only be valid when status is 'FAIL', so we can just
        pass in explicit None's for 'ok'.
        '''
        results = TestResults.TestResults()
        
        for suite in self.suites.keys():
            suiteName = suite.strip(")(")
            resultSuite = Suite.Suite(suiteName)
            
            for test, status in self.suites[suite]:
                resultTest = TestCase.TestCase(test)
                
                file, line = self._getFailInfo(suite, test)
                
                if status == "FAIL":
                    resultTest.addNotice(Notice.Notice(file, line, None, "fail"))
                elif status == "ok":
                    resultTest.addNotice(Notice.Notice(None, None, None, "pass"))
                    
                resultSuite.testCases.append(resultTest)
            
            results.suites.append(resultSuite)
            
        return results
    
    def _getFailInfo(self, suite, test):
        '''
        get file and line info for a failed test.
        
        Cleans up data and returns proper types.
        
        @return returns file and line if present. None if not found.
        @date Jun 29, 2010
        '''
        try:
            file, line = self.failSuites[suite][test]
            
            file = file.strip(',')
            file = file.strip('"')
            
            line = int(line.strip(','))
        except:
            file = line = None
            
        return (file, line)

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
        return re.match(PythonUnittestParser.VALID_STATUS_LINE_REGEX, line) is not None
    
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
        return re.match(PythonUnittestParser.VALID_FAIL_LINE_REGEX, line) is not None
    
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
        return re.match(PythonUnittestParser.VALID_FAIL_INFO_LINE_REGEX, line) is not None
