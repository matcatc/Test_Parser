'''
@date Feb 19, 2010
@author: Matthew A. Todd
'''
import INotice

class Message(INotice.INotice):
    '''
    contains a simple string message.
    @see INotice
    
    @date Feb 19,2010
    @author Matthew A. Todd
    '''

    _message = ""
    _file = ""
    _line = 0
    
    def __init__(self, file, line, message):
        '''
        Constructor
        
        message is a string.
        message can be empty, but it will raise a warning
        '''
        if file is None or line is None or message is None:
            raise ValueError("parameter to Error was None")
        
        if file is "":
            raise ValueError("file name is empty")
        
        if message is "":
            raise Warning("message is empty")
        
        if line < 0:
            raise ValueError("line number is negative")
                
        self._file = file
        self._line = line
        self._msg = message
        
    def getFile(self):
        return self._file    
    
    def getLine(self):
        return self._line
        
    def getMessage(self):
        return self._message