'''
@date Jul 6, 2010
@author: Matthew Todd

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
from TestParser.Model.JUnitRunner import JUnitRunner

class JUnitRunner_Test(unittest.TestCase):


    def setUp(self):
        self.runner = JUnitRunner()


    def tearDown(self):
        del self.runner


    def test_computeCmd(self):
        self.runner.runner = '<runner>'
        self.assertEquals(self.runner.computeCmd(['blah']), self.runner.runner)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()