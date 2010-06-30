'''
Created on Jun 30, 2010

@author: matcat
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
        output = [self.runner.runner]
        self.assertEqual(self.runner.computeCmd(input), output)
        
    def testRunAll(self):
        '''
        test runAll() with real input
        '''
        self.runner.runner = computeDataFilepath("python_unittest_example.py", __file__)
        stdout = self.runner.runAll()
        self.assertNotEqual(stdout, None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()