'''
@date Feb 22, 2010
@author: Matthew A. Todd
'''
from . import IParse
from ..TestResults import TestResults, Suite, TestCase, Notice

class BasicParser(IParse.IParse):
    '''
    Our basic parser.
    
    Notice types:
        - error
        - message
    
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
        
        # VERIFY go through all the suites, parsing and adding
        for suite in tree.getiterator():
            if suite.tag == "TestLog":
                results.suites.add(self._parseSuite(suite))
        
        
        return results
        
        
    def _parseSuite(self, suiteTree):
        suite = Suite.Suite()
        suite.name = suiteTree.get("name")
        
        # VERIFY go through all the tests, parsing and adding
        for test in suiteTree.getiterator():
            if test.tag == "TestSuite":
                suite.testCases.add(self._parseTestCase(test)) 
        
        return suite
    
    def _parseTestCase(self, testTree):
        test = TestCase.TestCase()
        
        if testTree.get("name") is not None:
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
