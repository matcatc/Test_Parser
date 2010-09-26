'''
Interface for Errors and Message types.

@date Feb 19, 2010
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

from TestParser.Common.Constants import CONSTANTS
from . import TestComponent

class Notice(TestComponent.TestComponent):
    '''
    Interface for Errors and Message types.
    
    Composite.
    
    Used in TestCase. This way, a single list can hold
    Errors and Messages in the order they occurred.
    The other option would be to keep them separate,
    thereby loosing information (the order they occurred.)
    @see TestCase
    
    @date Feb 19, 2010
    @author Matthew A. Todd
    '''
    
    EMPTY_INFO = "Warning: info is empty"
    EMPTY_TYPE = "Warning: type is empty"
    EMPTY_FILE = "Warning: file is empty"
    NEGATIVE_LINE = "Error: line number is negative"

    def __init__(self, file, line, info, type):
        '''
        Constructor
        
        @param file String containing the filename of where
            the notice occurred.
        @param line An integer of which line the notice occurred.
        @param type String describing the type of notice
            (i.e: Error, Message, or similar). If empty
            string, warning will be printed.
        @param info String describing the info to be stored
            in this notice. If empty string, warning will be printed.
            
        @see file.setter
        @see line.setter
        @see type.setter
        @see info.setter
        '''
        super().__init__(type)
        self.file = file
        self.line = line
        self.info = info

    def getChildren(self):
        return []
    
    def getRelevantDisplayData(self):
        line = None
        if self.line is not None:
            line = str(self.line) 
        return [("file", self.file),
                ("line", line),
                ("info", self.info)]
        
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self, file): #@DuplicatedSignature
        '''
        No longer throwing an exception if the filename is empty.
        What if the file info really isn't available for some reason?
        '''
        if file == "":
            CONSTANTS.logger.warning(Notice.EMPTY_FILE)
        self._file = file
    @file.deleter
    def file(self): #@DuplicatedSignature
        del self._file
       
    @property 
    def line(self):
        return self._line
    @line.setter
    def line(self, line): #@DuplicatedSignature
        '''
        @throw ValueError if line number is negative
        '''
        if line is None:
            self._line = None
            return
        if line < 0:
            CONSTANTS.logger.error(Notice.NEGATIVE_LINE)
            raise ValueError("line number is negative")
        self._line = line
    @line.deleter
    def line(self): #@DuplicatedSignature
        del self._line
        
    @property
    def info(self):
        return self._info
    @info.setter
    def info(self, info): #@DuplicatedSignature
        '''
        Will print warning to log if empty string
        '''
        if info == "":
            CONSTANTS.logger.warning(Notice.EMPTY_INFO)
        self._info = info
    @info.deleter
    def info(self): #@DuplicatedSignature
        del self._info
    
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type): #@DuplicatedSignature
        '''
        Will print warning to log if empty string
        '''
        if type == "":
            CONSTANTS.logger.warning(Notice.EMPTY_TYPE)
        self._type = type
    @type.deleter
    def type(self): #@DuplicatedSignature
        del self._type
