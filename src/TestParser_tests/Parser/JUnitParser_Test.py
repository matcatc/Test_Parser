'''
Created on Jul 6, 2010

@author: matcat
'''
import unittest
from TestParser.Parser.JUnitParser import JUnitParser
from TestParser.Common.computeDataFilepath import computeDataFilepath

class JUnitParser_Test(unittest.TestCase):


    def setUp(self):
        self.parser = JUnitParser()


    def tearDown(self):
        del self.parser

    def test_parseFile_3(self):
        f = open(computeDataFilepath("JUnit3_out", __file__))
        self.parser.parse(file = f)
        
    def test_parseFile_4(self):
        f = open(computeDataFilepath("JUnit4_out", __file__))
        self.parser.parse(file = f)

    def test_parseString(self):
        f = open(computeDataFilepath("JUnit4_out", __file__))
        self.parser.parse(stringData = f.read())
        
    def test_badStatusLine(self):
        data = '..Faa;dkadfjasdl\n'
        self.parser.parse( stringData=data)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()