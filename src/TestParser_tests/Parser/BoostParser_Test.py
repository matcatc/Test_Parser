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
from TestParser.Common.computeDataFilepath import computeDataFilepath

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
        data = '<TestLog>%s</TestLog>' % suite
        
        xml = ET.fromstring(data)
        results = self.parser._parseData(xml)
        
        self.assertEquals(results.suiteCount(), 1)

    def testParseSuite(self):
        name = "Sample_Test_Suite"
        test = '<TestCase name="Compute_Addition_Subtraction">\
            <TestingTime>0</TestingTime>\
        </TestCase>'
        
        testSuite = '<TestSuite name="%s">%s</TestSuite>' % (name, test)
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
        
        testCase = '<TestCase name="%(name)s"> \
            <Message file="%(file)s" line="%(line)d">%(message)s</Message> \
            <Error file="%(file)s" line="%(line)d">%(error)s</Error> \
            <TestingTime>%(time)d</TestingTime> \
        </TestCase>' % {'name' : name, 'file' : file, 'line' : line,
                         'message' : message, 'error':error, 'time':time}
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
        
    def test_testcaseFatalError(self):
        '''
        Test that parser handles FatalError.
        
        @date Jul 17, 2010
        '''
        name = 'test_fail'
        file = 'main.cpp'
        line = 36
        time = 0
        data = '<TestCase name="%(name)s"> \
                <FatalError file="%(file)s" line="%(line)d">Test fail</FatalError> \
                <TestingTime>%(time)d</TestingTime> \
            </TestCase>' % {'name':name, 'file' : file, 'line':line, 'time':time}
        
        xml = ET.fromstring(data)
        test = self.parser._parseTestCase(xml)
        
        self.assertEqual(test.type, "TestCase")
        self.assertEqual(test.name, name)
        self.assertEqual(test.timeTaken, time)
        
        self.assertEqual(len(test.notices), 1)
        notice = test.getChildren()[0]
        self.assertEqual(notice.type, "FatalError")
        self.assertEqual(notice.file, file)
        self.assertEqual(notice.line, line)
        
    def test_hierarchy(self):
        '''
        Test parse with real data.
        
        Tests with sub-suites. Checks that correct hierarchy returned.
        Doesn't test that all the data (names, lines, files, etc.) are
        correct, as it would complicate the test and its already checked
        in other tests.
        '''
        
        f = open(computeDataFilepath("./sample/boost.xml", __file__))
        results = self.parser.parse(file = f)
        
        lvl0 = results.getChildren()
        self.assertEquals(len(lvl0), 1)
        self.assertEquals(lvl0[0].type, "Suite")
        
        lvl1 = lvl0[0].getChildren()
        self.assertEquals(len(lvl1), 5)
        
        self.assertEquals(lvl1[0].type, "TestCase")
        
        self.assertEquals(lvl1[1].type, "TestCase")
        
        self.assertEquals(lvl1[2].type, "Suite")
        lvl2_a = lvl1[2].getChildren()
        self.assertEquals(len(lvl2_a), 2)
        self.assertEquals(lvl2_a[0].type, "TestCase")
        self.assertEquals(lvl2_a[1].type, "TestCase")
        
        self.assertEquals(lvl1[3].type, "Suite")
        lvl2_b = lvl1[3].getChildren()
        self.assertEquals(len(lvl2_b), 5)
        self.assertEquals(lvl2_b[0].type, "TestCase")
        self.assertEquals(lvl2_b[1].type, "TestCase")
        self.assertEquals(lvl2_b[2].type, "TestCase")
        self.assertEquals(lvl2_b[3].type, "TestCase")
        self.assertEquals(lvl2_b[4].type, "Suite")
        lvl3_a = lvl2_b[4].getChildren()
        self.assertEquals(len(lvl3_a), 1)
        self.assertEquals(lvl3_a[0].type, "TestCase")
        
        
        self.assertEquals(lvl1[4].type, "Suite")
        lvl2_c = lvl1[4].getChildren()
        self.assertEquals(len(lvl2_c), 2)
        self.assertEquals(lvl2_c[0].type, "TestCase")
        self.assertEquals(lvl2_c[1].type, "TestCase")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
