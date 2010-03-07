'''
Created on Mar 5, 2010

@author: matcat
'''
import unittest
from BoostTestParser.Parser import IParse

class IParse_Test(unittest.TestCase):


    def setUp(self):
        self.parser = IParse.IParse

    def tearDown(self):
        del self.parser

    def testParse(self):
        '''
        TODO: test parse()'s ability to handle different input.
        '''
        self.fail("Not implemented")

    def testparseData(self):
        '''
        IParse's parseData should be undefined.
        '''
        self.assertRaises(NotImplementedError, self.parser._parseData, None, None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
