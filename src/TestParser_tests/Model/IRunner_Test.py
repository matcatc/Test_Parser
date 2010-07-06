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

from TestParser.Model.IRunner import IRunner

class MockRunner(IRunner):
    '''
    IRunner leaves it to its children to implement computeCmd,
    so we're subclassing and implementing the most basic version
    so that we can test other functionality.
    '''
    def computeCmd(self, params):
        return self.runner + params
        

class IRunner_Test(unittest.TestCase):
    def setUp(self):
        self.runner = MockRunner()

    def tearDown(self):
        del self.runner

    
    def test_runnerDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.runner.runner = "blah"
        del self.runner.runner
    
    def test_InvalidRunner(self):
        '''
        test that when trying to run an invalid runner, nothing
        crazy happens.
        '''
        self.runner.runner = "invalid_runner_ALSKFJEOIJFDFLKJakjdflakjdfaedf"
        self.runner.run([])


    def test_NoneRunner(self):
        '''
        Test that return value is None when runner is None.
        
        Do we want run() to raise an exception instead?
        '''
        self.runner.runner = None
        stdout = self.runner.run([])
        
        self.assertEqual(stdout, None)
        
    
    def testRun_echo(self):
        '''
        test run() using echo.
        the "-n" option tells echo not to return a newline
        '''
        input = "echo test output"
        output = input + "\n"
        self.runner.runner = "echo"
        stdout = self.runner.run([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunPrevious_echo(self):
        '''
        test runPrevious() using echo.
        
        if runPrevious() actually executes same cmd, then the output should be
        the same.
        '''
        input = "test output"
        self.runner.runner = "echo"
        output1 = self.runner.run([input])
        
        output2 = self.runner.runPrevious()
        
        self.assertEqual(output1.decode("utf-8"), output2.decode("utf-8"))
        
    def testRunPrevious_Invalid(self):
        '''
        Test what happens when rerunning w/o a previous run. Should output
        to log and execute runAll().
        '''
        input = "echo test output"
        self.runner.runner = "echo"
        
        output1 = self.runner.runPrevious()
        
        output2 = self.runner.runAll()
        
        self.assertEqual(output1.decode("utf-8"), output2.decode("utf-8"))
        
        
    def testRunAll_echo(self):
        '''
        test runAll() using echo.
        output = "\n" b/c echo return a new line after printing (nothing in this case) 
        '''
        output = "\n"
        self.runner.runner = "echo"
        stdout = self.runner.runAll()
        self.assertEqual(stdout.decode("utf-8"), output)
    
    
    def test_computeCmd(self):
        '''
        Test that computeCmd() not implemented.
        '''
        runner = IRunner()
        self.assertRaises(NotImplementedError, runner.computeCmd, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()