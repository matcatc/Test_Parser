'''
@date Feb 22, 2010
@author: Matthew A. Todd
'''
import IParse
from BoostTestParser.TestResults import TestResults, Suite, Error, Message, TestCase

class BasicParser(IParse.IParse):
    '''
    Our basic parser
    
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
        # TODO go through all the suites, parsing and adding
        
        
        return results
        
        
    def _parseSuite(self, suiteTree):
        suite = Suite.Suite()
        # go through all the tests, parsing and adding
        
        return suite
    
    def _parseTestCase(self, testTree):
        test = TestCase.TestCase()
        
        test.setTimeTaken(testTree.get("name"))
        
        test.setName(testTree.find("TestingTime").text)
    
        iter = testTree.getiterator()
        for element in iter:
            file = element.get("file")
            line = element.get("line")
            text = element.text
            
            if element.tag is "Error":
                test.addError(Error.Error(file, line, text))
            elif element.tag is "Message":
                test.addMessage(Message.Message(file, line, text))
        
        return test