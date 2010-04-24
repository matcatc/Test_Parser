'''
@date Mar 6, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.Model.TestRunner import TestRunner
from BoostTestParser.Common.Constants import Constants
import io

class TestRunner_Test(unittest.TestCase):
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
    
    
    @date Mar 6, 2010
    @author: Matthew A. Todd
    '''


    def setUp(self):
        Constants.errStream = io.StringIO()
        self.runner = TestRunner()

    def tearDown(self):
        Constants.reset()
        del self.runner
        
    def test_runnerDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.runner.runner = "blah"
        del self.runner.runner

    def testRun_echo(self):
        '''
        test run() using echo.
        the "-n" option tells echo not to return a newline
        '''
        input = "echo test output"
        output = TestRunner.LOG_FORMAT + " --log_level=test_suite " + input + "\n"
        self.runner.runner = "echo"
        stdout = self.runner.run([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunAll_echo(self):
        '''
        test runAll() using echo.
        output = "\n" b/c echo return a new line after printing (nothing in this case) 
        '''
        output = TestRunner.LOG_FORMAT + " --log_level=test_suite\n"
        self.runner.runner = "echo"
        stdout = self.runner.runAll()
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunAll(self):
        '''
        test runAll() with real input
        this test depends on the the filesystem location from which we are running this test
        '''
        self.runner.runner = "tests/Model/Boost_Test"
        stdout = self.runner.runAll()
        self.assertNotEqual(stdout, None)

    def testRunTest_echo(self):
        '''
        test runTest() using echo
        '''
        self.runner.runner = "echo"
        
        input = "echo test output"
        output = TestRunner.LOG_FORMAT + " --log_level=test_suite --run_test=" + input + "\n"
        stdout = self.runner.runTest([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
        input1 = "test1"
        input2 = "test2"
        output = TestRunner.LOG_FORMAT + " --log_level=test_suite --run_test=" + input1 + "," + input2 + "\n"
        stdout = self.runner.runTest([input1, input2])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunTest(self):
        '''
        test runTest() with real input
        '''
        self.runner.runner = "tests/Model/Boost_Test"
        stdout = self.runner.runTest(["testA", "testB"])
        self.assertNotEqual(stdout, None)
        
    def testRunSuite(self):
        '''
        test runSuite() with real input
        '''
        self.runner.runner = "tests/Model/Boost_Test"
        stdout = self.runner.runSuite([])
        self.assertNotEqual(stdout, None)
        
    def test_InvalidRunner(self):
        '''
        test what happens when trying to run an invalid runner. i.e: we want
        an OSError to be thrown in run().
        
        None should be returned.
        An error message should be printed out to a given err stream.
        '''
        self.runner.runner = "invalid_runner_ALSKFJEOIJFDFLKJakjdflakjdfaedf"
        stdout = self.runner.run([])
        
        self.assertEqual(stdout, None)
        self.assertEqual(Constants.errStream.getvalue(), TestRunner.EXECUTION_FAILURE_MESSAGE + "\n")

    def test_NoneRunner(self):
        '''
        Test that return value is None when runner is None.
        
        Do we want run() to raise an exception instead?
        '''
        self.runner.runner = None
        stdout = self.runner.run([])
        
        self.assertEqual(stdout, None)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
