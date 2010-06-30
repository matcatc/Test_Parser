#!/usr/bin/python3
'''
@date Mar 25, 2010
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
import sys

from TestParser_tests.Common import Observable_Test, Observer_Test, UpdateJobPool_Test, UpdateThread_Test
from TestParser_tests.Model import Model_test, BoostRunner_test, PythonUnittestRunner_Test
from TestParser_tests.Parser import BoostParser_Test, PythonUnittestParser_Test, IParse_Test 
from TestParser_tests.TestResults import Notice_Test, Suite_Test, TestCase_Test, TestResults_Test, TestComponent_Test
from TestParser_tests.View import Controller_Test, TextView_Test, QtView_Test

def runTestSuites(testClasses):
    '''
    helper function that takes an iterable container of test suites
    and runs them all.
    '''
    suites = []
    for testClass in testClasses:
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        suites.append(suite)
        
    allSuite = unittest.TestSuite(suites)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(allSuite)

def main():
    runTestSuites([Observable_Test.Observable_Test, \
                   Observer_Test.Observer_Test, \
                    UpdateJobPool_Test.UpdateJobPool_Test, \
                     UpdateThread_Test.UpdateThread_Test, \
                      Model_test.Model_test, \
                       BoostRunner_test.BoostRunner_Test, \
                        PythonUnittestRunner_Test.PythonUnittestRunner_Test, \
                         BoostParser_Test.BoostParser_Test, \
                          PythonUnittestParser_Test.PythonUnittestParser_Test, \
                           IParse_Test.IParse_Test, \
                            Notice_Test.Notice_Test, \
                             Suite_Test.Suite_Test, \
                              TestCase_Test.TestCase_Test, \
                               TestResults_Test.TestResults_Test, \
                                TestComponent_Test.TestComponent_Test, \
                                 Controller_Test.ControllerTest, \
                                  TextView_Test.TextView_Test, \
                                   QtView_Test.QtView_Test])

if __name__ == '__main__':
    main()
