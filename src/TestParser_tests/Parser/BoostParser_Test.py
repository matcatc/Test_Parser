'''
@date Feb 27, 2010
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
from TestParser.Parser.BoostParser import BoostParser
from xml.etree import ElementTree as ET

class BoostParser_Test(unittest.TestCase):


    def setUp(self):
        self.parser = BoostParser()


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
        
        self.assertEqual(suite.name, name)
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
        
        self.assertEqual(test.name, name)
        self.assertEqual(test.timeTaken, time)
        self.assertEqual(len(test.notices), 2)
        
        for notice in test.notices:
            self.assertEqual(notice.line, line)
            self.assertEqual(notice.file, file)

        # check order and type of notices
        first = test.notices[0]
        self.assertEqual(first.info, message)
        second = test.notices[1]
        self.assertEqual(second.info, error)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
