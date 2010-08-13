'''
@date Jul 1, 2010
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

from TestParser.Common import TestFrameworkFactory

class TestFrameworkFactory_Test(unittest.TestCase):


    def setUp(self):
        self.framework = TestFrameworkFactory.TestFrameworkFactory()
        self.boost = TestFrameworkFactory._BoostFactory()
        self.python = TestFrameworkFactory._PythonUnittestFactory()
        self.junit = TestFrameworkFactory._JUnitFactory()

    def tearDown(self):
        del self.framework
        del self.boost
        del self.python
        del self.junit


    # Test FrameworkFactory
    def test_selectFramework(self):
        '''
        Test that select framework accepts valid inputs.
        Check for typos.
        '''
        TestFrameworkFactory.TestFrameworkFactory.selectFramework("Boost")
        TestFrameworkFactory.TestFrameworkFactory.selectFramework("PyUnittest")
        TestFrameworkFactory.TestFrameworkFactory.selectFramework("JUnit")
        
        self.assertRaises(TestFrameworkFactory.UndefinedTestFrameworkError,
                          TestFrameworkFactory.TestFrameworkFactory.selectFramework,
                          "nonexistent_framework")
    
    def test_createRunner(self):
        '''
        Test that nothing explodes
        '''
        TestFrameworkFactory.TestFrameworkFactory.selectFramework("Boost")
        
        TestFrameworkFactory.TestFrameworkFactory.createRunner()
        TestFrameworkFactory.TestFrameworkFactory.createParser()
        
    # Test BoostFactory
    def test_boostFactory(self):
        '''
        Test that methods are defined. Check for typos.
        '''
        self.boost.createParser()
        self.boost.createRunner()
    
    # Test PythonUnittestFactory
    def test_pythonUnittestFactory(self):
        '''
        Test that methods are defined. Check for typos.
        '''
        self.python.createParser()
        self.python.createRunner()
        
    def test_junitFactory(self):
        '''
        Test that methods are defined. Check for typos.
        '''
        self.junit.createParser()
        self.junit.createRunner()
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()