'''
@date Mar 24, 2010
@author Matthew A. Todd
'''
import unittest


class Model_test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_ResultsNotification(self):
        '''
        TODO: implement
        
        test that when results is changed, that observers are notified
        '''
        raise NotImplementedError
    
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