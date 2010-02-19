'''
Created on Feb 17, 2010

@author: Matthew A. Todd
'''
import Suite

class TestResults:
    '''
    classdocs
    '''
    
    _suites = set([])

    def __init__(self):
        '''
        Constructor
        '''
    
    def addSuite(self,suite):
        if suite is None:
            raise ValueError("suite is None")
        if not isinstance(suite, Suite):
            raise TypeError("suite is not of type Suite")
        
        self._suites.add(suite)
        
    def suiteCount(self):
        '''
        Returns the number of suites contained
        '''
        return len(self._suites)
        
        
    
