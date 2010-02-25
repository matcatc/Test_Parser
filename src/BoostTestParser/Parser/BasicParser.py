'''
@date Feb 22, 2010
@author: Matthew A. Todd
'''
import IParse
from BoostTestParser.TestResults import TestResults, Suite, TestCase, Notice

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
            results.addSuite(self._parseSuite(suite))
        
        
        return results
        
        
    def _parseSuite(self, suiteTree):
        suite = Suite.Suite()
        suite.setName(suiteTree.get("name"))
        
        # VERIFY go through all the tests, parsing and adding
        for test in suiteTree.getiterator():
            suite.addTest(self._parseTestCase(test)) 
        
        return suite
    
    def _parseTestCase(self, testTree):
        test = TestCase.TestCase()
        
        test.setTimeTaken(testTree.get("name"))
        
        test.setName(testTree.find("TestingTime").text)
    
        # VERIFY
        for element in testTree.getiterator():
            file = element.get("file")
            line = element.get("line")
            text = element.text
            
            if element.tag is "Error":
                test.add(Notice.Notice(file, line, text, "error"))
            elif element.tag is "Message":
                test.add(Notice.Notice(file, line, text, "message"))
        
        return test