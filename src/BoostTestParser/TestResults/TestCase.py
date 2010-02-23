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
    
    getMessages() and getErrors() isn't really needed. Just use getNotices()
    then check type of notice when displaying.
    
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
    
    def add(self, notice):
        if notice is None:
            raise NoneError("notice")
        
        if notice.isError():
            self._addError(notice)
        elif notice.isMessage(notice):
            self._addMessage(notice)
        # unknown data type
        else:
            self._addUnknown(notice)
            
    def _addUnknown(self, notice):
        self._notices.append(notice)        
    
    def _addError(self, error):        
        self._bError = True
        self._notices.append(error)
        
    def getErrors(self):
        '''
        parses the list looking for errors
        @return list of errors or empty list
        '''
        if not self.hasError():
            return []
        
        ret = []
        for notice in self._notices:
            if notice.isError():
                ret.append(notice)
        return ret
    
    
    def _addMessage(self, message):       
        self._notices.append(message)
        
    def getMessages(self):
        '''
        parses the list looking for messages
        @return list of messages or empty list
        '''
        ret = []
        for notice in self._notices:
            if notice.isMessage():
                ret.append(notice)
        return ret
    
    def getNotices(self):
        return self._notices
