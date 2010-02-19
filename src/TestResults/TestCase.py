'''
Created on Feb 17, 2010

@author: Matthew A. Todd
'''
import Error, Message


class TestCase:
    '''
    issue: if messages and errors are stored in separate data structures,
    the individual order will be lost
    
    >>> testCase = TestCase()
    >>> testCase.hasError()
    False
        
    >>> testCase.addError(0)    # not real error type, but works for test
    >>> testCase.hasError()
    True
    '''

    _bError = False      # whether TestCase contains error
    _notices = []
    _timeTaken = 0

    def __init__(self):
        '''
        Constructor
        '''
    
    def hasError(self):
        return self._bError
        
    def setTimeTaken(self, time):
        if time is None:
            raise ValueError("time is None")
        if time < 0:
            raise ValueError("time is negative")
        
        self._timeTaken = time
    
    
    def addError(self, error):
        if error is None:
            raise ValueError("error is None")
        if not isinstance(error, Error):
            raise TypeError("error is not of type Error")
        
        self._bError = True
        self._notices.append(error)
    
    
    def addMessage(self, message):
        if message is None:
            raise ValueError("message is None")
        if not isinstance(message, Message):
            raise TypeError("message is not of type Message")
        
        self._notices.append(message)
        