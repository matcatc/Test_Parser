'''
Created on Feb 26, 2010

@author: matcat
'''
import unittest
from BoostTestParser.TestResults.Suite import Suite
from BoostTestParser.TestResults.TestCase import TestCase
from BoostTestParser.TestResults.Notice import Notice

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
        self.test.addNotice(self.notice)
    

    def tearDown(self):
        self.suite.testCases.clear()
        del self.suite
        del self.test


    def testName(self):
        self.suite.name = self.name
        self.assertEqual(self.suite.name, self.name)

    def testCount(self):
        amount = 4
        
        for i in range(amount):
            test = TestCase()
            self.suite.testCases.add(test)
        
        self.assertEqual(self.suite.testCount(), amount)

    def testGetTestCases(self):
        self.suite.testCases.add(self.test)
        self.assertTrue(self.test in self.suite.testCases)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
