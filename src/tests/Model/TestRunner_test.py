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

    def testRun(self):
        output = "echo test output"
        self.runner.runner = "echo"
        stdout = self.runner.run(["-n", output])
        self.assertEqual(stdout.decode("utf-8"), output)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()