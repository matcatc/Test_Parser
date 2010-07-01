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

from TestParser.Common import FrameworkFactory

class FrameworkFactory_Test(unittest.TestCase):


    def setUp(self):
        self.framework = FrameworkFactory.FrameworkFactory()
        self.boost = FrameworkFactory._BoostFactory()
        self.python = FrameworkFactory._PythonUnittestFactory()


    def tearDown(self):
        del self.framework
        del self.boost
        del self.python


    # Test FrameworkFactory
    def test_selectFramework(self):
        '''
        Test that select framework accepts valid inputs.
        Check for typos.
        '''
        FrameworkFactory.FrameworkFactory.selectFramework("Boost")
        FrameworkFactory.FrameworkFactory.selectFramework("PyUnittest")
        
        self.assertRaises(FrameworkFactory.UndefinedTestFrameworkError,
                          FrameworkFactory.FrameworkFactory.selectFramework,
                          "nonexistent_framework")
    
    def test_framework(self):
        '''
        Test that abstract functions are undefined.
        '''
        self.assertRaises(NotImplementedError, self.framework.createRunner)
        self.assertRaises(NotImplementedError, self.framework.createParser)
    
    
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
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()