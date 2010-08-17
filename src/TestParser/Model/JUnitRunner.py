'''
@date Jul 4, 2010
@author matcat

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

class JUnitRunner(IRunner):
    '''
    classdocs
    @date Jul 4, 2010
    @author matcat
    '''


    def __init__(self):
        '''
        Constructor
        
        we're leaving it up to the user to use the (correct)
        JUnit test runner, then we don't need to know version information
        here.
        '''
        super().__init__()
    
    
    def computeCmd(self, params):
        '''
        Just run w/o any paramaters
        '''
        return self.runner