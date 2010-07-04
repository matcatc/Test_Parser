'''
@date Jul 3, 2010
@author Matthew A. Todd
'''

from . import IParse
from TestParser.Common.Constants import Constants

import re

class InvalidJUnitVersion(Exception):
    '''
    Raised when we have an invalid JUnit version.
    '''
    pass

class JUnitParser(IParse.IParse):
    '''
    Parser for JUnit 3 and 4.
    
    @date Jul 3, 2010
    @author Matthew A. Todd
    '''


    def __init__(self, version):
        '''
        Constructor
        
        @param version version number of Junit (i.e: 3 or 4).
        '''
        if version != 3 and version != 4:
            raise InvalidJUnitVersion()
        self.version = version

    def parse(self, file=None, stringData=None):
        '''
        '''
        if stringData is not None:
            self._parseData(stringData)
        elif file is not None:
            self._parseData(file.read())
        else:
            #TODO: raise
            Constants.logger.error("ERROR: parse() needs data to parse")
            return


    def _parseData(self, stringData):
        '''

        '''
        lines = stringData.split('\n')

        # If we're using JUnit 4, we need to remove the first line.
        if self.version == 4:
            lines.pop(0)

        statusLine = lines[0]
        testCount, errorCount, failCount = self._parseStatus(statusLine)

        failInfo = self._parseFailError(lines)
        
        Constants.logger.debug(str(failInfo))

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
        # TODO: verify statusLine w/ RegEx?
        # exception or None?

        Constants.logger.debug("statusLine = " + statusLine)

        testCount = len(re.findall('\.', statusLine))
        Constants.logger.debug("testCount = " + str(testCount))

        errorCount = len(re.findall('E', statusLine))
        Constants.logger.debug("errorCount = " + str(errorCount))

        failCount = len(re.findall('F', statusLine))
        Constants.logger.debug("failCount = " + str(failCount))

        return (testCount, errorCount, failCount)

    def _parseFailError(self, lines):
        '''
        Parses the fail and error messages to get data regarding the
        fails and errors.
        
        
        @see _parseFailError_JUnit4
        @see _parseFailError_JUnit3
        
        @return a list of tuples: (className, testName, fileName, line, exceptionLine),
            containing all the relevant fail/error message data (in order)
        @date Jul 3, 2010
        '''
        
        if self.version == 4:
            return self._parseFailError_JUnit4(lines)
        elif self.version == 3:
            Constants.logger.fatal("_parseFailError() hasn't implemented version 3 yet")
        else:
            raise InvalidJUnitVersion()


    def _parseFailError_JUnit4(self, lines):
        '''
        Parses the fail and error messages to get data regarding the
        fails and errors.
        
        format of fail/error messages:
        
        @verbatim
        #) testName(fileName)
        <error line>
            at class.test(file:line)
        @endverbatim
        
        example fail/error messages:
        
        @verbatim
        1) testTwo(test)
        java.lang.AssertionError: expected:<5> but was:<4>
            at org.junit.Assert.fail(Assert.java:91)
        
        2) TestThree(test)
        java.lang.Exception
            at test.TestThree(test.java:27)
    
        3) testFour(test)
        java.lang.AssertionError: 
            at org.junit.Assert.fail(Assert.java:91)
        @endverbatim
        
        Because when we find a matching line we need to get the next couple/next
        line(s), we're using an iterator. So when we find our match, we just
        ask for the needed next lines.
        
        @return a list of tuples: (className, testName, fileName, line, exceptionLine),
            containing all the relevant fail/error message data (in order)
        @date Jul 3, 2010
        
        TODO: pretty complex. Should we go for a BNF?
        '''
        failInfo = []
        
        lineIter = iter(lines)
        for line in lineIter:                
            bMatch = re.match(r"^[0-9]+\) [a-zA-Z0-9_]+\([a-zA-Z0-9_]+\)", line) is not None

            if bMatch:
                testLine = line
                Constants.logger.debug("line = " + testLine)
                
                words = testLine.split(' ')
                words = words[1].split('(')
                testName = words[0]
                className = words[1][:-1]
                Constants.logger.debug("testName = " + testName + "\tclassName = " + className)
                
                
                exceptionLine = next(lineIter)
                Constants.logger.debug("exceptionLine = " + exceptionLine)
                
                # look for locationLine that matches our testCase
                # should be something like: at className.testName(fileName:line)
                # TODO: potential to run into a StopIteration exception here
                found = False
                while not found: 
                    locationLine = next(lineIter)
                    
                    pattern = className+"\."+testName                        
                    if re.search(pattern, locationLine) is not None:
                        found = True
                    
                Constants.logger.debug("locationLine = " + locationLine)
                
                words2 = locationLine.split(' ')
                words2 = words2[1].split('(')
                words2 = words2[1][:-1].split(':')
                fileName = words2[0]
                line = words2[1]
                
                Constants.logger.debug("fileName = " + fileName + "\tline = " + line)
                
                failInfo.append( (className, testName, fileName, line, exceptionLine))
        return failInfo


    def _parseFailError_JUnit3(self, lines):
        '''
        Parses the fail and error messages to get data regarding the
        fails and errors.
        
        format of fail/error messages:
        
        @verbatim
        for JUnit3:
        #) testName(filename)<error line>
            at class.test(file:line)
        
        example fail/error messages:
        
        @verbatim        
        1) testTwo(Junit3_test)junit.framework.AssertionFailedError: expected:<5> but was:<4>
            at Junit3_test.testTwo(Junit3_test.java:20)
        @endverbatim
        
        @return a list of tuples: (className, testName, fileName, line, exceptionLine),
            containing all the relevant fail/error message data (in order)
        @date Jul 4, 2010
        '''
        pass

    def _compileTestResults(self):
        '''
        Using data that we've parsed, construct Test Results.
        
        @date Jul 3, 2010
        '''
        pass
