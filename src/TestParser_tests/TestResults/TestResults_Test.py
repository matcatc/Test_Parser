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

from TestParser.TestResults.TestResults import TestResults
from TestParser.TestResults.Suite import Suite

class TestResults_Test(unittest.TestCase):
    suite = Suite()

    def setUp(self):
        self.results = TestResults()


    def tearDown(self):
        del self.results.suites[:]
        del self.results
        
    def testSuiteCount(self):
        amount = 18
        for i in range(amount):
            suite = Suite()
            self.results.suites.append(suite)
            
        self.assertEqual(self.results.suiteCount(), amount)
        self.assertFalse(self.suite in self.results.suites)
        
    def testGetSuites(self):
        self.results.suites.append(self.suite)
        self.assertTrue(self.suite in self.results.suites)
        self.assertFalse(Suite() in self.results.suites)
        
    def test_getRelevantDisplayData(self):
        length = len(self.results.getRelevantDisplayData())
        self.assertEqual(length, 0)
        
    def test_getChildren(self):
        '''
        just check for typos
        and function is overridden
        '''
        self.results.getChildren()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()