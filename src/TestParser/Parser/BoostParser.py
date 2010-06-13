'''
@date Feb 22, 2010
@author: Matthew A. Todd

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

class BoostParser(IParse.IParse):
    '''
    Our basic parser for Boost's Test Framework.
    
    When looking at the code, I feel that it seems very "hard-coded."
    I assume there is probably a "better"/more dynamic way of structuring it
    so that all we have to give it is a couple data structures with strings
    of xml tags we're interested in. But, the hard-coded code is strait
    forward and easy to understand. Plus we don't want to get crazy until we
    have a couple other parsers anyways.  
    
    Notice types: @see _parseTestCase()
    
    @date Feb 22, 2010
    @author Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def _parseData(self, tree):
        '''
        @see IParse._parseData
        '''
        results = TestResults.TestResults()
        
        for suite in tree.getiterator():
            if suite.tag == "TestLog":
                results.suites.add(self._parseSuite(suite))
        
        
        return results
        
        
    def _parseSuite(self, suiteTree):
        suite = Suite.Suite()
        suite.name = suiteTree.get("name")
        
        for test in suiteTree.getiterator():
            if test.tag == "TestSuite":
                suite.testCases.add(self._parseTestCase(test)) 
        
        return suite
    
    def _parseTestCase(self, testTree):
        '''        
        Currently only deals with error and message notice types.
        We can easily add an else statement to handle unknown types,
        but I figured I should wait until there is a need.
        '''
        test = TestCase.TestCase()
        
        test.name = testTree.get("name")
            
        if testTree.find("TestingTime") is not None:
            test.timeTaken = int(testTree.find("TestingTime").text)
    
        for element in testTree.getiterator():
            file = element.get("file")
            if element.get("line") is not None:
                line = int(element.get("line"))
            text = element.text
            
            if element.tag == "Error":
                test.addNotice(Notice.Notice(file, line, text, "error"))
            elif element.tag == "Message":
                test.addNotice(Notice.Notice(file, line, text, "message"))
        
        return test
