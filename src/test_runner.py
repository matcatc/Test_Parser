'''
Created on Mar 25, 2010

@author: matcat
'''
import unittest
import sys

from tests.Common import Observable_Test
from tests.Model import Model_test, TestRunner_test
from tests.Parser import BasicParser_Test, IParse_Test 
from tests.TestResults import Notice_Test, Suite_Test, TestCase_Test, TestResults_Test

def runTestSuites(testClasses):
    suites = []
    for testClass in testClasses:
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        suites.append(suite)
        
    allSuite = unittest.TestSuite(suites)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(allSuite)

def main():
    runTestSuites([Observable_Test.Observable_Test, \
                   Model_test.Model_test, \
                    TestRunner_test.TestRunner_Test, \
                     BasicParser_Test.BasicParser_Test, \
                      IParse_Test.IParse_Test, \
                       Notice_Test.Notice_Test, \
                        Suite_Test.Suite_Test, \
                         TestCase_Test.TestCase_Test, \
                          TestResults_Test.TestResults_Test])

if __name__ == '__main__':
    main()
