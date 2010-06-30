'''
Created on Jun 30, 2010

@author: matcat
'''
import unittest

from TestParser.Parser.PythonUnittestParser import PythonUnittestParser
from TestParser.Common.computeDataFilepath import computeDataFilepath

class PythonUnittestParser_Test(unittest.TestCase):


    def setUp(self):
        self.parser = PythonUnittestParser()


    def tearDown(self):
        del self.parser

    def test_validStatusLine(self):
        self.assertTrue(self.parser._validStatusLine("test_choice123 (__main__.TestSequenceFunctions123) ... ok"))
        self.assertTrue(self.parser._validStatusLine("test_error (__main__.TestSequenceFunctions) ... ERROR"))
        self.assertTrue(self.parser._validStatusLine("test_fail (__main__.TestSequenceFunctions) ... FAIL"))
        
    def test_validFailLine(self):
        self.assertTrue(self.parser._validFailLine("FAIL: test_fail123 (__main__.TestSequenceFunctions123)"))
        self.assertTrue(self.parser._validFailLine("ERROR: test_error (__main__.TestSequenceFunctions)"))
        
    def test_validFailInfoLine(self):
        self.assertTrue(self.parser._validFailInfoLine('  File "python_unittest_example.py", line 43, in test_error'))
        self.assertTrue(self.parser._validFailInfoLine('  File "python_unittest_example.123asd", line 40123, in test_fail'))
    
    def test_ParseFile(self):
        f = open(computeDataFilepath("python_unittest_sample", __file__))
        self.parser.parse(file = f)
        
    def test_ParseStringdata(self):
        f = open(computeDataFilepath("python_unittest_sample", __file__))
        self.parser.parse(stringData = f.read())
        
    def test_ParseNone(self):
        '''
        Test that nothing explodes when we don't give it data to parse.
        
        Note: later we might change to checking for an exception.
        '''
        self.parser.parse(None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()