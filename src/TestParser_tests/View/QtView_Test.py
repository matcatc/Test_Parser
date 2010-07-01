'''
@date Apr, 25, 2010
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

#from TestParser.View.QtView import QtView

class QtView_Test(unittest.TestCase):
    '''
    
    @see TestRunner_test for information regarding how Boost_Test may
    cause tests that use it to fail.
    '''


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        raise NotImplementedError


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()