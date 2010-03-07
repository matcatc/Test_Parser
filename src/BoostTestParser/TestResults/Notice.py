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
        file, info, and type are of type String
        line is an int
        
        @param type: the type of notice (i.e: Error, Message, or similar)
        
        info can be an empty string, but a warning will be printed if it is.
        same for type.
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
        if info =="":
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
        if type == "":
            print("Warning: type is empty", file=sys.stderr)
        self._type = type
    @type.deleter
    def type(self): #@DuplicatedSignature
        del self._type
        
    def toString(self):
        return "%s in %s at line %d: %s" % (self.type, self.file, self.line, self.info)