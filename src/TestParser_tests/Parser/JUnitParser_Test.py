'''
Created on Jul 6, 2010

@author: matcat
'''
import unittest
from TestParser.Parser.JUnitParser import JUnitParser, UnknownLineType
from TestParser.Parser.JUnitYaccer import InvalidLine
from TestParser.Common.computeDataFilepath import computeDataFilepath

class JUnitParser_Test(unittest.TestCase):


    def setUp(self):
        self.parser = JUnitParser()


    def tearDown(self):
        del self.parser

    def test_parseFile_3(self):
        f = open(computeDataFilepath("./sample/JUnit3_out", __file__))
        self.parser.parse(file = f)
        
    def test_parseFile_4(self):
        f = open(computeDataFilepath("./sample/JUnit4_out", __file__))
        self.parser.parse(file = f)

    def test_parseString(self):
        f = open(computeDataFilepath("./sample/JUnit4_out", __file__))
        self.parser.parse(stringData = f.read())
        
    def test_badStatusLine(self):
        data = '..Faa;dkadfjasdl\n'
        self.parser.parse( stringData=data)
        
    def test_parseNone(self):
        '''
        Test what happens when we don't give data to parse.
        '''
        self.assertRaises(ValueError, self.parser.parse, None)
        
    def test_parse(self):
        '''
        Test and validate parse with real data.
        '''
        data = open(computeDataFilepath("./sample/JUnit4_out", __file__)).read()
        
        results = self.parser.parse(stringData = data)
        
        testPass = results.getChildren()[0]
        noticePass = testPass.getChildren()[0]
        self.assertEquals(noticePass.type, "pass")
        
        suite = results.getChildren()[1]
        suiteData = suite.getRelevantDisplayData()
        self.assertTrue(('name', 'test') in suiteData)
        
        tests = suite.getChildren()
        self.assertEquals(len(tests), 3)
        
        test0 = tests[0]
        test0_data = test0.getRelevantDisplayData()
        self.assertTrue(('name', 'testTwo') in test0_data)
        notice0 = test0.getChildren()[0]
        self.assertEquals(notice0.type, 'fail')
        notice0_data = notice0.getRelevantDisplayData()
        self.assertTrue(('file', 'test.java') in notice0_data)
        self.assertTrue(('line', '21') in notice0_data)
        self.assertTrue(('info', 'java.lang.AssertionError: expected : < 5 > but was : < 4 >') in notice0_data)
        
        test1 = tests[1]
        test1_data = test1.getRelevantDisplayData()
        self.assertTrue(('name', 'TestThree') in test1_data)
        notice1 = test1.getChildren()[0]
        self.assertEquals(notice1.type, 'fail')
        notice1_data = notice1.getRelevantDisplayData()
        self.assertTrue(('file', 'test.java') in notice1_data)
        self.assertTrue(('line', '27') in notice1_data)
        self.assertTrue(('info', 'java.lang.Exception'))
        
        test2 = tests[2]
        test2_data = test2.getRelevantDisplayData()
        self.assertTrue(('name', 'testFour') in test2_data)
        notice2 = test2.getChildren()[0]
        self.assertEquals(notice2.type, 'fail')
        notice2_data = notice2.getRelevantDisplayData()
        self.assertTrue(('file', 'test.java') in notice2_data)
        self.assertTrue(('line', '33') in notice2_data)
        self.assertTrue(('info', 'java.lang.AssertionError') in notice2_data)
        
        
    ## tests for exceptions
    def test_UnknownLineType(self):
        '''
        Test that nothing explodes
        '''
        exception = UnknownLineType("nonexistent_test_line_type")
        str(exception)
        repr(exception)
        
    
    def test_InvalidLine(self):
        '''
        Test that nothing explodes
        '''
        exception = InvalidLine()
        str(exception)
        repr(exception)
        
        exception = InvalidLine(3)
        str(exception)
        repr(exception)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()