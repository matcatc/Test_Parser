'''
Created on Feb 17, 2010

@author: matcat
'''

class TestResults:
    '''
    classdocs
    '''
    
    suites = set([])

    def __init__(self, suites):
        '''
        Constructor
        '''
        self.suites = set(suites)
    
    def addSuite(self,suite):
        self.suites.add(suite)
        
    def suiteCount(self):
        '''
        Returns the number of suites contained
        '''
        return len(self.suites)
        
        
    
