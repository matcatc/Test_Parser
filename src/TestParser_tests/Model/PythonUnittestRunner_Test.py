'''
@date Jun 30, 2010
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

from TestParser.Model.PythonUnittestRunner import PythonUnittestRunner
from TestParser.Common.computeDataFilepath import computeDataFilepath

class PythonUnittestRunner_Test(unittest.TestCase):


    def setUp(self):
        self.runner = PythonUnittestRunner()


    def tearDown(self):
        del self.runner


    def test_computeCmd(self):
        '''
        Test that the command returned is correct
        '''
        self.runner.runner = "<runner>"
        input = ["input"]
        output = self.runner.runner
        self.assertEqual(self.runner.computeCmd(input), output)
        
    def testRunAll(self):
        '''
        test runAll() with real input
        '''
        self.runner.runner = computeDataFilepath("./sample/python_unittest_example.py", __file__)
        stdout = self.runner.runAll()
        self.assertNotEqual(stdout, None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()