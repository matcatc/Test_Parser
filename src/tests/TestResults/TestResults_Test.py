'''
Created on Feb 26, 2010

@author: matcat
'''
import unittest

from BoostTestParser.TestResults.TestResults import TestResults
from BoostTestParser.TestResults.Suite import Suite

from BoostTestParser.Exception.NoneError import NoneError

#TODO

class Test(unittest.TestCase):
    suite = Suite()

    def setUp(self):
        self.results = TestResults()


    def tearDown(self):
        self.results._suites.clear()
        del self.results


    def testAddSuite(self):
        self.assertRaises(NoneError, self.results.addSuite, None)
        
    def testSuiteCount(self):
        amount = 18
        for i in range(amount):
            suite = Suite()
            self.results.addSuite(suite)
            
        self.assertEqual(self.results.suiteCount(), amount)
        self.assertFalse(self.suite in self.results.getSuites())
        
    def testGetSuites(self):
        self.results.addSuite(self.suite)
        self.assertTrue(self.suite in self.results.getSuites())
        self.assertFalse(Suite() in self.results.getSuites())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()