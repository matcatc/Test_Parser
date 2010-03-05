'''
Created on Feb 26, 2010

@author: matcat
'''
import unittest

from BoostTestParser.TestResults.TestResults import TestResults
from BoostTestParser.TestResults.Suite import Suite

class Test(unittest.TestCase):
    suite = Suite()

    def setUp(self):
        self.results = TestResults()


    def tearDown(self):
        self.results.suites.clear()
        del self.results
        
    def testSuiteCount(self):
        amount = 18
        for i in range(amount):
            suite = Suite()
            self.results.suites.add(suite)
            
        self.assertEqual(self.results.suiteCount(), amount)
        self.assertFalse(self.suite in self.results.suites)
        
    def testGetSuites(self):
        self.results.suites.add(self.suite)
        self.assertTrue(self.suite in self.results.suites)
        self.assertFalse(Suite() in self.results.suites)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()