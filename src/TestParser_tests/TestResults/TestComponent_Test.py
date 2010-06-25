'''
@date Jun 25, 2010
@author: Matthew A. Todd
'''
import unittest
from TestParser.TestResults.TestComponent import TestComponent

class TestComponent_Test(unittest.TestCase):


    def setUp(self):
        self.component = TestComponent('unittest')


    def tearDown(self):
        del self.component

    def test_getChildren(self):
        '''
        Test that raises NotImplementedError
        '''
        self.assertRaises(NotImplementedError,
                          self.component.getChildren)
    
    def test_getRelevantDisplayData(self):
        '''
        Test That raises NotImplementedError
        '''
        self.assertRaises(NotImplementedError,
                          self.component.getRelevantDisplayData)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()