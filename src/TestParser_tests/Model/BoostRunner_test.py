'''
@date Mar 6, 2010
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
from TestParser.Model.BoostRunner import BoostRunner
from TestParser.Common.Constants import Constants
from TestParser.Common.computeDataFilepath import computeDataFilepath
import io

class BoostRunner_Test(unittest.TestCase):
    '''
    For the tests that use Boost_Test, I'm not sure if
    they will work on Windows because the file is a linux
    compiled file. But the changes necessary aren't that
    difficult to make. If you come up with a better way
    of implementing the test, such that its easier to
    switch binaries, or you want me to, please let me
    know.
    
    Boost_Test is just a compiled version of the source
    code found here:
    http://www.boost.org/doc/libs/1_42_0/libs/test/doc/html/utf/user-guide/runtime-config/run-by-name.html
    
    @warning The tests that use Boost_Test will fail if access to
        Boost_Test is denied by the OS. This happens when TestParser has
        been installed in a virtualenv, for instance.
    
    @date Mar 6, 2010
    @author: Matthew A. Todd
    '''


    def setUp(self):
        Constants.errStream = io.StringIO()
        self.runner = BoostRunner()

    def tearDown(self):
        Constants.reset()
        del self.runner

    def testRunAll(self):
        '''
        test runAll() with real input
        '''
        self.runner.runner = computeDataFilepath("Boost_Test", __file__)
        stdout = self.runner.runAll()
        self.assertNotEqual(stdout, None)

    def testRunTest_echo(self):
        '''
        test runTest() using echo
        '''
        self.runner.runner = "echo"
        
        input = "echo test output"
        output = BoostRunner.LOG_FORMAT + " --log_level=test_suite --run_test=" + input + "\n"
        stdout = self.runner.runTest([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
        input1 = "test1"
        input2 = "test2"
        output = BoostRunner.LOG_FORMAT + " --log_level=test_suite --run_test=" + input1 + "," + input2 + "\n"
        stdout = self.runner.runTest([input1, input2])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunTest(self):
        '''
        test runTest() with real input
        '''
        self.runner.runner = computeDataFilepath("Boost_Test", __file__)
        stdout = self.runner.runTest(["testA", "testB"])
        self.assertNotEqual(stdout, None)
        
    def testRunSuite(self):
        '''
        test runSuite() with real input
        '''
        self.runner.runner = computeDataFilepath("Boost_Test", __file__)
        stdout = self.runner.runSuite([])
        self.assertNotEqual(stdout, None)
        
    def test_computeCmd(self):
        '''
        Test that the command returned is correct
        '''
        self.runner.runner = "<runner>"
        input = ["input"]
        output = self.runner.runner + [BoostRunner.LOG_FORMAT, "--log_level=test_suite"] + input
        self.assertEqual(self.runner.computeCmd(input), output)
        

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
