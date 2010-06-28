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

import sys

class PythonUnittestParser(IParse.IParse):
    '''
    Parser for Python's unittest framework
    
    @date Jun 27, 2010
    @author Matthew A. Todd
    '''


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
        else:
            self._parseData(file.read())
            
        return self._compileTestResults()
    
    def _parseData(self, stringData):
        '''
        Parses the given string data and sets it up in self.suites
        for later compiling
        
        @param stringData all the data contained w/in a string
        '''
        lines = stringData.split('\n')
        
        for line in lines:
            words = line.split(' ')
            
            # TODO: use regEx to validate instead
            if len(words) > 3:
                name = words[0]
                suite = words[1]
                status = words[3]
                
#                print("DEBUG: name = ", name,
#                      "\n\tsuite = ", suite,
#                      "\n\tstatus = ", status,
#                      file=sys.stderr)
                
                if suite not in self.suites:
                    self.suites[suite] = []
                    
                self.suites[suite].append((name, status))
            else:
                return
            
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
                print("DEBUG: name = ", name,
                        "\tstatus = ", status,
                        file=sys.stderr)
                resultTest = TestCase.TestCase(name)
                
                if status == "FAIL":
                    resultTest.addNotice(Notice.Notice(None, None, None, "fail"))
                elif status == "ok":
                    resultTest.addNotice(Notice.Notice(None, None, None, "pass"))
                    
                resultSuite.testCases.append(resultTest)
            
            results.suites.append(resultSuite)
            
        return results
            

            
            
