'''
A single test case

@date Feb 17, 2010
@author: Matthew A. Todd
'''

class TestCase(object):
    '''
    A single test. Which may have multiple errors (asserts).
    
    Messages and errors are contained in one list, so that the order in which
    they occurred is not lost. This is why they both inherit INotice.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.notices = []
        self.types = set()          # set of known types (of notices added)
        self._timeTaken = 0
        self.name = ""
    
    def hasType(self, type):
        '''
        whether test case has a given type of notice
        '''
        return type in self.types
    
    @property
    def timeTaken(self):
        return self._timeTaken
    @timeTaken.setter
    def timeTaken(self, time): #@DuplicatedSignature
        if time < 0:
            raise ValueError("time is negative")
        self._timeTaken = time        
    @timeTaken.deleter
    def timeTaken(self): #@DuplicatedSignature
        del self._timeTaken

    
    def addNotice(self, notice):
        '''
        @param notice: notice to add
        '''          
        self.types.add(notice.type)
        self.notices.append(notice)
    
    def getNoticesOfType(self, type):
        '''
        parses the list of notices, looking for those of a given type
        @param type type of notices to return
        @return list of notices of type type
        '''
        ret = []
        for notice in self.notices:
            if notice.type == type:
                ret.append(notice)
        return ret
