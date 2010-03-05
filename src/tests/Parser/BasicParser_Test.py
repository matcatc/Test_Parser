'''
Created on Feb 27, 2010

@author: matcat
'''
import unittest
from BoostTestParser.Parser.BasicParser import BasicParser
from xml.etree import ElementTree as ET

class BasicParser_Test(unittest.TestCase):


    def setUp(self):
        self.parser = BasicParser()


    def tearDown(self):
        del self.parser

    def testParseData(self):
        suite = '<TestSuite name="Expression_Solver_Unit_Tests">\
                <TestCase name="Compute_Addition_Subtraction">\
                    <TestingTime>0</TestingTime>\
                </TestCase>\
            </TestSuite>'
        data = '<TestLog>' + suite +'</TestLog>'
        
        xml = ET.fromstring(data)
        results = self.parser._parseData(xml)
        
        self.assertEquals(results.suiteCount(), 1)

    def testParseSuite(self):
        name = "Sample_Test_Suite"
        test = '<TestCase name="Compute_Addition_Subtraction">\
            <TestingTime>0</TestingTime>\
        </TestCase>'
        
        testSuite = '<TestSuite name="' + name + '">'\
            + test\
            + '</TestSuite>'
        xml = ET.fromstring(testSuite)
        suite = self.parser._parseSuite(xml)
        
        self.assertEqual(suite.getName(), name)
        self.assertEqual(suite.testCount(), 1)
        

    def testParseTestCase(self):        
        name = "sampleTestCase"
        file = "main.cpp"
        line = 10
        message = "sample message"
        error = "sample error"
        time = 0
        
        testCase = '<TestCase name="' + name + '"> \
            <Message file="' + file + '" line="' + str(line) + '">' + message + '</Message> \
            <Error file="' + file + '" line="' + str(line) + '">' + error + '</Error> \
            <TestingTime>' + str(time) + '</TestingTime> \
        </TestCase>'
        xml = ET.fromstring(testCase)
        test = self.parser._parseTestCase(xml)
        
        self.assertEqual(test.getName(), name)
        self.assertEqual(test.getTimeTaken(), time)
        self.assertEqual(len(test.getNotices()), 2)
        
        for notice in test.getNotices():
            self.assertEqual(notice.getLine(), line)
            self.assertEqual(notice.getFile(), file)

        # check order and type of notices
        first = test.getNotices()[0]
        self.assertEqual(first.getInfo(), message)
        second = test.getNotices()[1]
        self.assertEqual(second.getInfo(), error)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
