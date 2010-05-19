'''
@date Mar 24, 2010
@author Matthew A. Todd
'''
import unittest
from BoostTestParser.Model import Model
from BoostTestParser.Model import TestRunner
from BoostTestParser.Parser import BasicParser
from ..Common.Observable_Test import Mock_Observer


class Model_test(unittest.TestCase):
    
    runner = TestRunner.TestRunner()
    runner.runner = "tests/Model/Boost_Test"
    parser = BasicParser.BasicParser()
    
    data = '<TestSuite name="test suite">\
                <TestCase name="test testCase">\
                    <TestingTime>0</TestingTime>\
                </TestCase>\
            </TestSuite>'

    def setUp(self):
        self.model = Model.Model()

    def tearDown(self):
        del self.model
        
    def test_resultsDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.model.results = "blah"
        del self.model.results

    def test_NoneParser(self):
        '''
        test what happens when parser is None and method(s) are called
        '''
        self.assertRaises(AttributeError, self.model._doParse, Model_test.data)
        
    def test_NoneTestRunner(self):
        '''
        test what happens when testRunner is None and method(s) are called
        '''
        self.assertRaises(AttributeError, self.model.runAll)

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
        test that results change, are not None
        test that nothing is thrown, etc with some real data (typos, etc)
        '''
        self.model.parser = Model_test.parser
        
        oldResults = self.model.results
        self.model._doParse(Model_test.data)
        
        self.assertTrue(self.model.results is not None)
        self.assertNotEqual(self.model.results, oldResults)
    
    def test_runAll(self):
        '''
        test that results change, are not None
        test that runAll doesn't throw anything when given real data (typos, etc.)
        '''
        self.model.testRunner = Model_test.runner
        self.model.parser = Model_test.parser
        
        oldResults = self.model.results
        
        self.model.runAll()
        
        self.assertTrue(self.model.results is not None)
        self.assertNotEqual(self.model.results, oldResults)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()