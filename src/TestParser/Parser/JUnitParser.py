'''
@date Jul 3, 2010
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
from TestParser.Common.Constants import CONSTANTS
from ..TestResults import TestResults, Suite, TestCase, Notice
from .JUnitYaccer import InvalidLine, yaccer                #@UnresolvedImport


import re


class UnknownLineType(Exception):
    '''
    Used when Yaccer returns a line_type that we don't know how to
    handle and aren't expecting.
    
    This deserves an exception because it shows that there is a bug,
    as it should only be returning the line types we know and handle.
    
    @date Jul 6, 2010
    @author Matthew A. Todd 
    '''
    def __init__(self, lineType):
        self.lineType = lineType
    def __str__(self):
        return "Unknown Line Type: %s" % self.lineType
    def __repr__(self):
        return str(self)


class JUnitParser(IParse.IParse):
    '''
    Parser for JUnit 3 and 4.
    
    We managed to combine the JUnit 3 and 4 code such that we don't
    need to know which version we're working with. Benefit is that
    we don't have to worry about user specifying incorrect version.
    
    @date Jul 3, 2010
    @author Matthew A. Todd
    '''

    # matches line: 'JUnit version #.#.#'
    JunitVersionLine_Regex = re.compile(r'^JUnit version [0-9\.]+$')

    def __init__(self):
        '''
        Constructor
        '''

    def parse(self, file=None, stringData=None):
        '''
        '''
        if stringData is not None:
            return self._parseData(stringData)
        elif file is not None:
            return self._parseData(file.read())
        else:
            CONSTANTS.logger.error("parse() needs data to parse")
            raise ValueError("parse() needs data to parse")


    def _parseData(self, stringData):
        '''
        Overall function that coordinates the parsing and compilation
        of data.
        
        Only real work it does is removes the first line if its a
        JUnit version identifier. That way the code will work with
        both JUnit3 and JUnit4.
        '''
        lines = stringData.split('\n')

        # JUnit4 will print an extra line: 'JUnit version #.#.#'
        #  which we remove to unify the two JUnits
        if JUnitParser.JunitVersionLine_Regex.match(lines[0]):
            lines.pop(0)

        statusLine = lines[0]
        testCount, errorCount, failCount = self._parseStatus(statusLine)

        failInfo = self._parseFailError(lines)
        CONSTANTS.logger.debug(str(failInfo))
        
        suites = self._compileSuites(failInfo)
        CONSTANTS.logger.debug(str(suites))
        
        return self._compileTestResults(testCount, errorCount, failCount, suites)

    def _parseStatus(self, statusLine):
        '''
        Parse the status line.
        
        statusLine is of the following form:
        @verbatim
        ....E.F.E...
        @/endverbatim
        
        @return (testCount, errorCount, failCount) tuple
        @date Jul 3, 2010
        '''
        # need to use BNF to completely verify,
        # but this is more of a sanity check
        if not re.match(r'^[\.EF]+$', statusLine):
            CONSTANTS.logger.error("statusLine isn't of correct form")
            # TODO: raise?

        CONSTANTS.logger.debug("statusLine = %s" % statusLine)

        testCount = len(re.findall('\.', statusLine))
        CONSTANTS.logger.debug("testCount = %d" % testCount)

        errorCount = len(re.findall('E', statusLine))
        CONSTANTS.logger.debug("errorCount = %d" % errorCount)

        failCount = len(re.findall('F', statusLine))
        CONSTANTS.logger.debug("failCount = %d" % failCount)

        return (testCount, errorCount, failCount)

    def _parseFailError(self, lines):
        '''
        Parses the fail and error messages to get data regarding the
        fails and errors.

        format of fail/error messages:
        
        @verbatim
        JUnit4:
        
        #) testName(fileName)
        <error line>
            at class.test(file:line)
            
        JUnit3:
        
        #) testName(filename)<error line>
            at class.test(file:line)
        @endverbatim
        
        example fail/error messages:
        
        @verbatim
        JUnit4: 
        
        1) testTwo(test)
        java.lang.AssertionError: expected:<5> but was:<4>
            at org.junit.Assert.fail(Assert.java:91)
        
        2) TestThree(test)
        java.lang.Exception
            at test.TestThree(test.java:27)
    
        3) testFour(test)
        java.lang.AssertionError: 
            at org.junit.Assert.fail(Assert.java:91)
        
        JUnit3:    
        
        1) testTwo(Junit3_test)junit.framework.AssertionFailedError: expected:<5> but was:<4>
            at Junit3_test.testTwo(Junit3_test.java:20)
        @endverbatim
        
        
        Uses PLY (python lex yacc) to break down the lines, validate, and
        return the relevant data. Then takes said data and assembles it
        into list failInfo, to be used later in the program.
        
        @return a list of tuples: (className, testName, fileName, line, exceptionLine),
            containing all the relevant fail/error message data (in order)
        @date Jul 3, 2010
        '''
        failInfo = []
        
        # TODO: we need to reset variables after each add to failInfo?
        # Seems to work without it, but it feels a little weird
        
        for line in lines:
            try:
                temp = yaccer.parse(line)                   #@UndefinedVariable
                if temp is not None:
                    lineType = temp[0]
                    lineDict = temp[1]
                    
                    if lineType == 'status_line_junit3':
                        testName = lineDict['testName']
                        suiteName = lineDict['suiteName']
                        
                        exception = lineDict['exception']
                        exceptionData = lineDict['info']

                        if exceptionData is not None:                        
                            info = "%s: %s" % (exception, exceptionData)
                        else:
                            info = exception
                    
                    elif lineType == 'status_line':
                        testName = lineDict['testName']
                        suiteName = lineDict['suiteName']
                        
                    elif lineType == 'exception_line':
                        exception = lineDict['exception']
                        exceptionData = lineDict['info']

                        if exceptionData is not None:                        
                            info = "%s: %s" % (exception, exceptionData)
                        else:
                            info = exception
                            
                    elif lineType == 'detail_line':
                        classData = lineDict['class']
                        
                        # check that the file and line occur in the test and suite
                        # should have all necessary data now.
                        if classData == "%s.%s" % (suiteName, testName):
                            fileName = lineDict['filename']
                            line = lineDict['line']
                        
                            failInfo.append( (suiteName, testName, fileName, line, info))
                            
                    else:
                        CONSTANTS.logger.error("encountered unknown line type %s" % lineType)
                        raise UnknownLineType(lineType)
                    
            except InvalidLine:
                # We just got a line that yacc doesn't know how to handle.
                # We don't need to do anything. see JUnit4Yaccer.
                pass
        
        return failInfo


    
    def _compileSuites(self, failInfo):
        '''
        Takes information from _parseFailError() and breaks it into suites.
        
        failInfo is a list of tuples (suiteName, testName, fileName, line, info).
        So all the tests from the same suite aren't currently grouped together.
        Which is why this method exists.        
        
        @date Jul 4, 2010
        @author Matthew A. Todd
        '''
        suites = {}
        
        for suite, test, filename, line, info in failInfo:
            if suite not in suites:
                suites[suite] = []
                
            suites[suite].append((test, filename, line, info))
        
        return suites
        

    def _compileTestResults(self, testCount, errorCount, failCount, suites):
        '''
        Using data that we've gathered, construct Test Results.
        
        @date Jul 3, 2010
        '''
        results = TestResults.TestResults()
        
        bad = errorCount + failCount
        good = testCount - bad
        
        # add good tests
        for i in range(good):                                   #@UnusedVariable
            resultTest = TestCase.TestCase()
            resultTest.addNotice(Notice.Notice(None, None, None, "pass"))
            
            results.suites.append(resultTest)
        
        # add bad suites
        for suite in suites.keys():
            suiteName = suite
            resultSuite = Suite.Suite(suiteName)
            
            for test, filename, line, info in suites[suite]:
                resultTest = TestCase.TestCase(test)
                
                resultTest.addNotice(Notice.Notice(filename, line, info, "fail"))
                    
                resultSuite.testCases.append(resultTest)
            
            results.suites.append(resultSuite)

        return results
