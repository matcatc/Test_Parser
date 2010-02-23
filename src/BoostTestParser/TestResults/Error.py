'''
@date Feb 17, 2010
@author: Matthew A. Todd
'''
import INotice

class Error(INotice.INotice):
    '''
    An error
    @see INotice
    
    @date Feb 17, 2010
    @date Matthew A. Todd
    '''

    _file = ""
    _line = 0
    _error = ""     # can be empty, but should be noted

    def __init__(self, file, line, error):
        '''
        file and error are of type String
        line is an int
        
        error can be an empty string, but a warning will be sent if it is
        '''
        if file is None or line is None or error is None:
            raise ValueError("parameter to Error was None")
        
        if file is "":
            raise ValueError("file name is empty")
        
        if error is "":
            raise Warning("error is empty string")
        
        if line < 0:
            raise ValueError("line number is negative")
        
        self._file = file
        self._line = line
        self._error = error

    def getFile(self):
        return self._file
    
    def getLine(self):
        return self._line
    
    def getError(self):
        return self._error
        
    def toString(self):
        return "in %s at line %d: %s" % (self.getFile(), self.getLine(), self.getError())