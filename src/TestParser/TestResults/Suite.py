'''
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

class Suite:
    '''
    Contains an entire suite of tests. Organized into test cases.
    

    @date Feb 17, 2010
    @author Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.testCases = set([])
        self.name = ""
        
    def testCount(self):
        '''
        Number of tests cases contained in this suite
        @return number of tests contained in suite.
        '''
        return len(self.testCases)
        
