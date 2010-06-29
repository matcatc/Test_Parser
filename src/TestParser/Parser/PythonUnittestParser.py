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

class PythonUnittestParser(IParse.IParse):
    '''
    Parser for Python's unittest framework
    
    @date Jun 27, 2010
    @author Matthew A. Todd
    '''
    
    ## for use in _validStatusLine()
    REGEX = r'^[a-zA-z0-9_]+ \([a-zA-z0-9_.]+\) \.{3} (FAIL|ok)$'

    def __init__(self):
        '''
        Constructor
        '''
        self.suites = {}
    
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
        for later compiling
        
        @param stringData all the data contained w/in a string
        '''
        lines = stringData.split('\n')
        
        for line in lines:
            temp = self._validStatusLine(line)
            Constants.logger.debug("line = " + line + "\n\tvalid = " + str(temp))
            if temp:
                words = line.split(' ')
                name = words[0]
                suite = words[1]
                status = words[3]
                
                if suite not in self.suites:
                    self.suites[suite] = []
                    
                self.suites[suite].append((name, status))
            
    def _compileTestResults(self):
        '''
        Takes the data contained in self.suites and puts it in TestResults
        for returning. 
        '''
        results = TestResults.TestResults()
        
        for suite in self.suites.keys():
            suiteName = suite.strip(")(")
            resultSuite = Suite.Suite(suiteName)
            
            for name, status in self.suites[suite]:
                resultTest = TestCase.TestCase(name)
                
                if status == "FAIL":
                    resultTest.addNotice(Notice.Notice(None, None, None, "fail"))
                elif status == "ok":
                    resultTest.addNotice(Notice.Notice(None, None, None, "pass"))
                    
                resultSuite.testCases.append(resultTest)
            
            results.suites.append(resultSuite)
            
        return results
            

    def _validStatusLine(self, line):
        '''
        Uses regex to validate that the given line contains data to extract.
        For use on the one-liner status lines that appear at the beginning
        of python unittest's output.
        
        Line should be of the form:
        
        @verbatim
        name (suite) ... status
        @endverbatim
        
        Where name and suite are valid python identifiers. Except that
        suite can (and probably will) have a '.'.
        Status is either 'FAIL' or 'ok'.
        
        @warning Its entirely possible that I've missed certain characters
        than can appear (particularly in name and suite.)
        
        @param line line to check
        @return true if line is valid
        @date Jun 29, 2010 
        '''
        return re.match(PythonUnittestParser.REGEX, line) is not None
            
