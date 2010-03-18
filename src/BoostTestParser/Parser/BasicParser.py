'''
@date Feb 22, 2010
@author: Matthew A. Todd
'''
from . import IParse
from ..TestResults import TestResults, Suite, TestCase, Notice

class BasicParser(IParse.IParse):
    '''
    Our basic parser.
    
    Notice types: @see _parseTestCase()
    
    @date Feb 22, 2010
    @author: Matthew A. Todd
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
