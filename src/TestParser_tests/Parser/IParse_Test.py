'''
@date Mar 5, 2010
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
import os.path
from TestParser.Parser import IParse
from TestParser.Common.computeDataFilepath import computeDataFilepath

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

    def testparse(self):
        '''
        IParse's parse() should be undefined.
        '''
        self.assertRaises(NotImplementedError, self.parser.parse, None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
