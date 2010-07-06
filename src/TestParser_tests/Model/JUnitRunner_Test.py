'''
Created on Jul 6, 2010

@author: matcat
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