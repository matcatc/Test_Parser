'''
@date Jun 28, 2010
@author Matthew A. Todd

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
from .IRunner import IRunner

class PythonUnittestRunner(IRunner):
    '''
    Runner for Python Unittest framework.
    
    @warning Because of how Python Unittest is designed, we require
    that the test runner be setup a certain way. For parsing to work,
    we need the verbosity level to be set to 2. For running to work,
    we need the information all output to stdout. I.e: use the
    following command in your test runner.
    
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    
    @date Jun 28, 2010
    @author Matthew A. Todd
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
    
    
    def computeCmd(self, params):
        '''
        Just run w/o any paramaters
        '''
        return [self.runner]
