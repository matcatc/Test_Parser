'''
@author: Matthew A. Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''
from . import TestComponent

class TestCase(TestComponent.TestComponent):
    '''
    A single test. Which may have multiple errors (asserts).
    
    Messages and errors are contained in one list, so that the order in which
    they occurred is not lost. This is why they both inherit INotice.
    
    @date Feb 17, 2010
    @author Matthew A. Todd
    '''

    def __init__(self, name = ""):
        '''
        Constructor
        '''
        super().__init__("TestCase")
        self.notices = []
        ## set of known types (of notices added)
        self.types = set()          
        self._timeTaken = 0
        self.name = name
        
    def getChildren(self):
        return self.notices
    
    def getRelevantDisplayData(self):
        return [("name", self.name),
                 ("time", str(self.timeTaken))]
    
    def hasType(self, type):
        '''
        Whether test case has a given type of notice
        
        @return True if notice of type type contained in list of notices
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
        @param notice notice to add
        '''          
        self.types.add(notice.type)
        self.notices.append(notice)
    
    def getNoticesOfType(self, type):
        '''
        Parses the list of notices, looking for those of a given type.
        Returns list of all of those found (in order they were found.)
        
        @param type type of notices to return
        @return list of notices of type type
        '''
        ret = []
        for notice in self.notices:
            if notice.type == type:
                ret.append(notice)
        return ret
