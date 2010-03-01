'''
A single test case

@date Feb 17, 2010
@author: Matthew A. Todd
'''
from BoostTestParser.Exception.NoneError import NoneError

class TestCase:
    '''
    A single test. Which may have multiple errors (asserts).
    
    Messages and errors are contained in one list, so that the order in which
    they occurred is not lost. This is why they both inherit INotice.
    
    >>> testCase = TestCase()
    >>> testCase.hasType("error")
    False
        
    >>> testCase.add(0, "error")    # not real error type, but works for test
    >>> testCase.hasType("error")
    True
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._notices = []
        self._types = set()          # set of known types (of notices added)
        self._timeTaken = 0
        self._name = ""
    
    def hasType(self, type):
        '''
        whether test case has a given type of notice
        '''
        return type in self.getTypes()
    
    def getTypes(self):
        return self._types
        
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
        '''
        @param notice: notice to add
        '''
        if notice is None:
            raise NoneError("notice")
        
        self._addNotice(notice, notice.getType())           
        
            
    def _addNotice(self, notice, type):
        self._types.add(type)
        self._notices.append(notice)        
    
    def getNotices(self):
        return self._notices
    
    def getNoticesOfType(self, type):
        '''
        parses the list of notices, looking for those of a given type
        @param type type of notices to return
        @return list of notices of type type
        '''
        ret = []
        for notice in self.getNotices():
            if notice.getType() == type:
                ret.append(notice)
        return ret
