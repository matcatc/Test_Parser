'''
Created on Mar 5, 2010

@author: matcat
'''
import unittest
import xml.etree
import os.path
from BoostTestParser.Parser import IParse

class Mock_Parser(IParse.IParse):
    '''
    subclass IParse so that we can make sure that the correct
    data is being passed to _parseData()
    '''
    def _parseData(self, tree):
        self.tree = tree
        

class IParse_Test(unittest.TestCase):


    def setUp(self):
        self.parser = IParse.IParse()
        self.mockParser = Mock_Parser()

    def tearDown(self):
        del self.parser

    def testParseStringData(self):
        '''
        test parse() when given some string data
        
        Use Mock_Parser so that we can have access to tree,
        which is the data that is passed into _parseData()
        '''
        data = '<TestSuite name="test suite">\
                <TestCase name="test testCase">\
                    <TestingTime>0</TestingTime>\
                </TestCase>\
            </TestSuite>'
        self.mockParser.parse(stringData = data)
        
        tree = self.mockParser.tree
        self.assertTrue(tree is not None)
        self.assertTrue(isinstance(tree, xml.etree.ElementTree._Element))
        
        
        
    def testParseFilename(self):
        '''
        test parse() when given a filename 
        
        Use Mock_Parser so that we can have access to tree,
        which is the data that is passed into _parseData()
        '''
        filename = "tests/Parser/xml"
        self.mockParser.parse(file=os.path.abspath(filename))
        
        tree = self.mockParser.tree
        self.assertTrue(tree is not None)
        self.assertTrue(isinstance(tree, xml.etree.ElementTree.ElementTree))

    def testparseData(self):
        '''
        IParse's parseData should be undefined.
        '''
        self.assertRaises(NotImplementedError, self.parser._parseData, None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
