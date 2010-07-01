'''
Created on Jul 1, 2010

@author: matcat
'''
import unittest

from TestParser.Common import FrameworkFactory

class FrameworkFactory_Test(unittest.TestCase):


    def setUp(self):
        self.framework = FrameworkFactory.FrameworkFactory()
        self.boost = FrameworkFactory.BoostFactory()
        self.python = FrameworkFactory.PythonUnittestFactory()


    def tearDown(self):
        del self.framework
        del self.boost
        del self.python


    # Test FrameworkFactory
    def test_selectFramework(self):
        '''
        Test that select framework accepts valid inputs.
        Check for typos.
        '''
        FrameworkFactory.FrameworkFactory.selectFramework("Boost")
        FrameworkFactory.FrameworkFactory.selectFramework("PyUnittest")
        
        self.assertRaises(FrameworkFactory.UndefinedTestFrameworkError,
                          FrameworkFactory.FrameworkFactory.selectFramework,
                          "nonexistent_framework")
    
    def test_framework(self):
        '''
        Test that abstract functions are undefined.
        '''
        self.assertRaises(NotImplementedError, self.framework.createRunner)
        self.assertRaises(NotImplementedError, self.framework.createParser)
    
    
    # Test BoostFactory
    def test_boostFactory(self):
        '''
        Test that methods are defined. Check for typos.
        '''
        self.boost.createParser()
        self.boost.createRunner()
    
    # Test PythonUnittestFactory
    def test_pythonUnittestFactory(self):
        '''
        Test that methods are defined. Check for typos.
        '''
        self.python.createParser()
        self.python.createRunner()
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()