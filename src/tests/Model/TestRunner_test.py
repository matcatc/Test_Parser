'''
@date Mar 6, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.Model.TestRunner import TestRunner


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
        self.runner = TestRunner()

    def tearDown(self):
        del self.runner

    def testRun_echo(self):
        '''
        test run() using echo.
        the "-n" option tells echo not to return a newline
        '''
        input = "echo test output"
        output = TestRunner.format + " --log_level=test_suite " + input + "\n"
        self.runner.runner = "echo"
        stdout = self.runner.run([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunAll_echo(self):
        '''
        test runAll() using echo.
        output = "\n" b/c echo return a new line after printing (nothing in this case) 
        '''
        output = TestRunner.format + " --log_level=test_suite\n"
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
        output = TestRunner.format + " --log_level=test_suite --run_test=" + input + "\n"
        stdout = self.runner.runTest([input])
        self.assertEqual(stdout.decode("utf-8"), output)
        
        input1 = "test1"
        input2 = "test2"
        output = TestRunner.format + " --log_level=test_suite --run_test=" + input1 + "," + input2 + "\n"
        stdout = self.runner.runTest([input1, input2])
        self.assertEqual(stdout.decode("utf-8"), output)
        
    def testRunTest(self):
        '''
        test runTest() with real input
        '''
        self.runner.runner = "tests/Model/Boost_Test"
        stdout = self.runner.runTest(["testA", "testB"])
        self.assertNotEqual(stdout, None)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
