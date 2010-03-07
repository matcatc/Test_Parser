'''
Created on Mar 6, 2010

@author: matcat
'''
import unittest
from BoostTestParser.Model.TestRunner import TestRunner

# TODO: delete if not needed
#import sys

class TestRunner_Test(unittest.TestCase):


    def setUp(self):
        self.runner = TestRunner()

    def tearDown(self):
        del self.runner

    def testRun_echo(self):
        '''
        test run() using echo.
        the "-n" option tells echo not to return a newline
        '''
        output = "echo test output"
        self.runner.runner = "echo"
        stdout = self.runner.run(["-n", output])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunAll_echo(self):
        '''
        test runAll() using echo.
        output = "\n" b/c echo return a new line after printing (nothing in this case) 
        '''
        output = "\n"
        self.runner.runner = "echo"
        stdout = self.runner.runAll()
        self.assertEqual(stdout.decode("utf-8"), output)

    def testRunTest_echo(self):
        '''
        test runTest() using echo
        '''
        self.runner.runner = "echo"
        
        input = "echo test output"
        output = "--run_test=" + input + "\n"
        stdout = self.runner.runTest([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
        input1 = "test1"
        input2 = "test2"
        output = "--run_test=" + input1 + "," + input2 + "\n"
        stdout = self.runner.runTest([input1, input2])
        self.assertEqual(stdout.decode("utf-8"), output)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
