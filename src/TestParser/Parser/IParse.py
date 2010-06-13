'''
@date Feb 22, 2010
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

from xml.etree import ElementTree as ET

class IParse():
    '''
    Parsing interface.
    A strategy.
    
    Classes that implement this interface are to parse XML and return a TestResults (import TestResults).
    They do so by implementing _parseData().
    
    @date Feb 22, 2010
    @author Matthew A. Todd 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def parse(self, file=None, stringData=None):
        '''
        Delegates to _parseData()
        @see _parseData()
        
        TODO: verify this works for possible input types
        
        stringData has a higher priority than file. So if both are provided,
        stringData will be used.
        
        @pre stringData or the data contained in file need to be xml parsable
        by xml.etree.ElementTree. I assume any well formed xml will be fine.
        
        @param stringData a string containing the xml data.
        @param file a filename or file object.
        @return TestResults containing the parsed results
        '''
        if stringData is not None:
            tree = ET.fromstring(stringData)
            return self._parseData(tree)
        else:
            tree = ET.parse(file)
            return self._parseData(tree.getroot())
        
    def _parseData(self, tree):
        '''
        Builds up a TestResults with the given xml data.
        
        Is to be implemented in subclass
        
        @param tree an ElementTree with all of the xml data
        @return TestResults 
        '''
        raise NotImplementedError