'''
@date Feb 26, 2010
@author: Matthew A. Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

import unittest
from TestParser.TestResults.Suite import Suite
from TestParser.TestResults.TestCase import TestCase
from TestParser.TestResults.Notice import Notice

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
