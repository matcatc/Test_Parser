'''
@date Jun 23, 2010
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

class TestComponent(object):
    '''
    Abstract class for Test Results Composite pattern (Component.)
    
    
    @verbatim
    Example:
    TestResults
        Suite
            TestCase
                Notice (Error / Message)
    @endverbatim
    
                    
    @see TestResults.dia for more information (doc folder)
    
    @date Jun 23, 2010
    @author Matthew A. Todd
    '''


    def __init__(self, type):
        '''
        Constructor
        '''
        self.type = type
        
    def getChildren(self):
        '''
        Get all children/composed items.
        
        To be implemented in subclasses.
        '''
        raise NotImplementedError
    
    def getRelevantDisplayData(self):
        '''
        Returns all the data to be displayed as a list of tuples: (infotype, data)
        where infotype is line, file, name, etc and data is a string.
        
        Views can then use this information to display how they please.
        They can just output it strait, using infotype to explain what data
        is (TextView.) Or they can check infotype to see what to do with
        the data (QtView.)
        
        Note: because type is already provided in this class here
         (TestComponent,) I'm not packaging it in subclasses.
         
        Note: the order of the tuples MAY have an effect upon the order
        the data is displayed. If the data isn't parsed, for instance.
        '''
        raise NotImplementedError