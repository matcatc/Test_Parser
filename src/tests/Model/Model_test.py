'''
@date Mar 24, 2010
@author Matthew A. Todd
'''
import unittest
from BoostTestParser.Model import Model
from ..Common.Observable_Test import Mock_Observer

class Model_test(unittest.TestCase):
    # TODO: static testRunner
    # TODO: static parser

    def setUp(self):
        self.model = Model.Model()


    def tearDown(self):
        del self.model

    # TODO: test what happens when no runner and/or parser is None
    def test_NoneParser(self):
        '''
        test what happens when parser is None and method(s) are called
        
        TODO: implement
        '''
        raise NotImplementedError
        
    def test_NoneTestRunner(self):
        '''
        test what happends when testRunner is None and method(s) are called
        
        TODO: implement
        '''
        raise NotImplementedError

    def test_ResultsNotification(self):
        '''
        Test that when results is changed, that observers are notified.
        
        We use nonsensical data in this test, but the actual value isn't
        used, therefore its fine.
        
        We need a mock observer, so we're using Observable_Test's
        '''
        observer = Mock_Observer()
        self.model.registerObserver(observer)
        
        self.model.results = "data"
        self.assertTrue(observer.notified)
    
    def test_doParse(self):
        '''
        TODO: implement
        
        test that results change, are not None
        test that nothing is thrown, etc with some real data (typos, etc)
        '''
        raise NotImplementedError
    
    def test_runAll(self):
        '''
        TODO: implement
        
        test that results change, are not None
        test that runAll doesn't throw anything when given real data (typos, etc.)
        '''
        raise NotImplementedError


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()