'''
Created on Feb 26, 2010

@author: matcat
'''
import unittest
from BoostTestParser.TestResults.Suite import Suite
from BoostTestParser.TestResults.TestCase import TestCase
from BoostTestParser.TestResults.Notice import Notice

from BoostTestParser.Exception.NoneError import NoneError

class Suite_Test(unittest.TestCase):
    file = "suite.cpp"
    line = 36
    info = "suite blah"
    type = "error"
    notice = Notice(file, line, info, type)
    
    name = "testSuite"
 
                        
    def setUp(self):
        self.suite = Suite()

        self.test = TestCase()
        self.test.add(self.notice, self.notice)
    

    def tearDown(self):
        del self.suite._testCases[:]
        del self.suite
        del self.test


    def testName(self):
        self.suite.setName(self.name)
        self.assertEqual(self.suite.getName(), self.name)

    def testCount(self):
        amount = 4
        
        for i in range(amount):
            self.suite.addTest(self.test)
        
        self.assertEqual(self.suite.testCount(), amount)
        
    def testAddTest(self):
        self.assertRaises(NoneError, self.suite.addTest, None)

    def testGetTestCases(self):
        amount = 12
        for i in range(amount):
            self.suite.addTest(self.test)
            
        self.assertTrue(self.test in self.suite.getTestCases())
        self.assertEqual(len(self.suite.getTestCases()), amount)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
