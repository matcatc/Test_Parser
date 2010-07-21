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
        f = open(computeDataFilepath("./sample/python_unittest_sample", __file__))
        self.parser.parse(file = f)
        
    def test_ParseStringdata(self):
        f = open(computeDataFilepath("./sample/python_unittest_sample", __file__))
        self.parser.parse(stringData = f.read())
        
    def test_ParseNone(self):
        '''
        Test that nothing explodes when we don't give it data to parse.
        
        Note: later we might change to checking for an exception.
        '''
        self.parser.parse(None)

    
    def test_Parse(self):
        '''
        Test and validate with real data.
        
        Everything is hardcoded. I did this b/c its easy, fast, simple and
        provides unobfuscated documentation.
        
        Note: order of tests isn't guaranteed.
        TODO: Find a better way to test such that we don't have to specify the order.
        
        @date Jul 13, 2010
        '''
        data = open(computeDataFilepath("./sample/python_unittest_sample", __file__)).read()
        
        results = self.parser.parse(stringData = data)
        
        suites = results.getChildren()
        self.assertEquals(len(suites), 1)
        
        suite = suites[0]
        suiteData = suite.getRelevantDisplayData()
        self.assertTrue(('name', '__main__') in suiteData)
        
        subSuites = suite.getChildren()
        self.assertEqual(len(subSuites), 1)
        
        subSuite = subSuites[0]
        subSuiteData = subSuite.getRelevantDisplayData()
        self.assertTrue(('name', 'TestSequenceFunctions') in subSuiteData)
        
        tests = subSuite.getChildren()
        self.assertEqual(len(tests), 5)
        
        test0 = tests[0]
        test0_data = test0.getRelevantDisplayData()
        self.assertTrue(('name', 'test_shuffle') in test0_data)
        notice0 = test0.getChildren()[0] 
        self.assertEquals(notice0.type, "ok")
        
        test1 =tests[1]
        test1_data = test1.getRelevantDisplayData()
        self.assertTrue(('name', 'test_fail') in test1_data)
        notice1 = test1.getChildren()[0]
        self.assertEquals(notice1.type, "fail")
        notice1_data = notice1.getRelevantDisplayData()
        self.assertTrue(('file', 'python_unittest_example.py') in notice1_data)
        self.assertTrue(('line', '40') in notice1_data)
        self.assertTrue(('info', "AssertionError: None") in notice1_data)
        
        test2 = tests[2]
        test2_data = test2.getRelevantDisplayData()
        self.assertTrue(('name', 'test_sample') in test2_data)
        notice2 = test2.getChildren()[0]
        self.assertEquals(notice2.type, "ok")
        
        test3 = tests[3]
        test3_data = test3.getRelevantDisplayData()
        self.assertTrue(('name', 'test_choice') in test3_data)
        notice3 = test3.getChildren()[0]
        self.assertEquals(notice3.type, "ok")
        
        test4 = tests[4]
        test4_data = test4.getRelevantDisplayData()
        self.assertTrue(('name', 'test_error') in test4_data)
        notice4 = test4.getChildren()[0]
        self.assertEquals(notice4.type, "error")
        notice4_data = notice4.getRelevantDisplayData()
        self.assertTrue(('file', 'python_unittest_example.py') in notice4_data)
        self.assertTrue(('line', '43') in notice4_data)
        self.assertTrue(('info', "NotImplementedError") in notice4_data)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()