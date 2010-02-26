'''
Interface for Errors and Message types.

@date Feb 19, 2010
@author: Matthew A. Todd
'''

from BoostTestParser.Exception import NoneError

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


    _file = ""
    _line = 0
    _info = ""     # can be empty, but should be noted
    _type = ""

    def __init__(self, file, line, info, type):
        '''
        file, info, and type are of type String
        line is an int
        
        @param type: the type of notice (i.e: Error, Message, or similar)
        
        info can be an empty string, but a warning will be sent if it is
        '''
        if file is None or line is None or info is None or type is None:
            raise NoneError("some parameter")
        
        if file == "":
            raise ValueError("file name is empty")
        
        if info == "":
            raise Warning("info is empty string")
        
        if type == "":
            raise Warning("type is empty string")
        
        if line < 0:
            raise ValueError("line number is negative")
        
        self._file = file
        self._line = line
        self._info = info
        self._type = type.lower()

    def getFile(self):
        return self._file
    
    def getLine(self):
        return self._line
    
    def getInfo(self):
        return self._error
    
    def getType(self):
        return self._type
        
    def toString(self):
        return "%s in %s at line %d: %s" % (self.getType(), self.getFile(), self.getLine(), self.getInfo())