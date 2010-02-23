'''
@date Feb 22, 2010
@author: Matthew A. Todd
'''
import IParse
import TestResults

class BasicParser(IParse):
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
        suite = TestResults.Suite()
        # go through all the tests, parsing and adding
        
        return suite
    
    def _parseTestCase(self, testTree):
        test = TestResults.TestCase()
        
        test.setTimeTaken(testTree.get("name"))
        
        test.setName(testTree.find("TestingTime").text)
    
        iter = testTree.getiterator()
        for element in iter:
            file = element.get("file")
            line = element.get("line")
            text = element.text
            
            if element.tag is "Error":
                test.addError(TestResults.Error(file, line, text))
            elif element.tag is "Message":
                test.addMessage(TestResults.Message(file, line, text))

            

        
        return test