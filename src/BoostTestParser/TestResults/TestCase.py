'''
A single test case

@date Feb 17, 2010
@author: Matthew A. Todd
'''
from BoostTestParser.Exception import NoneError

class TestCase:
    '''
    A single test. Which may have multiple errors (asserts).
    
    Messages and errors are contained in one list, so that the order in which
    they occurred is not lost. This is why they both inherit INotice.
    
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
    _name = ""
    ERROR = 1
    MESSAGE = 2

    def __init__(self):
        '''
        Constructor
        '''
    
    def hasError(self):
        return self._bError
        
    def setTimeTaken(self, time):
        if time is None:
            raise NoneError("time")
        if time < 0:
            raise ValueError("time is negative")
        
        self._timeTaken = time
        
    def getTimeTaken(self):
        return self._timeTaken    
    
    def setName(self, name):
        self._name = name
        
    def getName(self):
        return self._name
    
    def addError(self, error):
        if error is None:
            raise NoneError("error")
        
        self._bError = True
        self._notices.append( (self.ERROR, error))
        
    def getErrors(self):
        '''
        parses the list looking for errors
        @return list of errors or empty list
        '''
        if not self.hasError():
            return []
        
        ret = []
        for noticeTup in self._notices:
            if noticeTup[0] is self.ERROR:
                ret.append(noticeTup[1])
        return ret
    
    
    def addMessage(self, message):
        if message is None:
            raise NoneError("message")
        
        self._notices.append( (self.MESSAGE, message))
        
    def getMessages(self):
        '''
        parses the list looking for messages
        @return list of messages or empty list
        '''
        ret = []
        for noticeTup in self._notices:
            if noticeTup[0] is self.MESSAGE:
                ret.append(noticeTup[1])
        return ret