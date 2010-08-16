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
from xml.etree import ElementTree as ET

class BoostParser(IParse.IParse):
    '''
    Our basic parser for Boost's Test Framework.
    
    @date Feb 22, 2010
    @author Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def parse(self, file=None, stringData=None):
        '''
        Delegates to _parseData()
        @see _parseData()
        
        stringData has a higher priority than file. So if both are provided,
        stringData will be used.
        
        @pre stringData or the data contained in file need to be xml parsable
        by xml.etree.ElementTree. I assume any well formed xml will be fine.
        
        @param stringData a string containing the xml data.
        @param file a filename or file object.
        @return TestResults containing the parsed results
        '''
        if stringData is not None:
            tree = ET.fromstring(stringData)
            return self._parseData(tree)
        else:
            tree = ET.parse(file)
            return self._parseData(tree.getroot())
        

    def _parseData(self, tree):
        '''
        Recursive function that parses Boost Test results.
        
        @date Jul 17, 2010
        '''
        
        if tree.tag == "TestCase":
            return self._parseTestCase(tree)
        
        elif tree.tag == "TestLog":
            results = TestResults.TestResults()
            for child in tree:
                temp = self._parseData(child)
                if temp is not None:
                    results.suites.append(temp)
            return results
            
        elif tree.tag == "TestSuite":
            suite = Suite.Suite()
            for child in tree:
                temp = self._parseData(child)
                if temp is not None:
                    suite.testCases.append(temp)
            return suite
        
        
    def _parseSuite(self, suiteTree):
        suite = Suite.Suite()
        suite.name = suiteTree.get("name")
        
        for test in suiteTree.getiterator():
            if test.tag == "TestSuite":
                suite.testCases.append(self._parseTestCase(test)) 
        
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
            elif element.tag == "FatalError":
                test.addNotice(Notice.Notice(file, line, text, "FatalError"))
            elif element.tag == "Message":
                test.addNotice(Notice.Notice(file, line, text, "message"))
            elif element.tag == "Info":
                if text == "check true passed":
                    test.addNotice(Notice.Notice(file, line, text, "pass"))
                else:
                    test.addNotice(Notice.Notice(file, line, text, "info"))
        
        return test
