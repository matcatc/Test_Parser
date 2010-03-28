'''
Interface for Errors and Message types.

@date Feb 19, 2010
@author: Matthew A. Todd
'''
import sys

class Notice():
    '''
    Interface for Errors and Message types.
    Used in TestCase. This way, a single list can hold
    Errors and Messages in the order they occurred.
    The other option would be to keep them separate,
    thereby loosing information (the order they occurred.)
    @see TestCase
    
    @date Feb 19, 2010
    @author Matthew A. Todd
    '''

    def __init__(self, file, line, info, type):
        '''
        Constructor
        
        @param file String containing the filename of where
            the notice occurred.
        @param line An int of which line the notice occurred.
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
        self.file = file
        self.line = line
        self.info = info
        self.type = type
        
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self, file): #@DuplicatedSignature
        '''
        @throw ValueError if file name is empty
        '''
        if file == "":
            raise ValueError("file name is empty")
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
        if line < 0:
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
        Will print warning to stderr if empty string
        '''
        if info == "":
            print("Warning: info is empty", file=sys.stderr)
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
        Will print warning to stderr if empty string
        '''
        if type == "":
            print("Warning: type is empty", file=sys.stderr)
        self._type = type
    @type.deleter
    def type(self): #@DuplicatedSignature
        del self._type