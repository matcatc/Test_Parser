'''
Contain the entire results from a run of tests.

Structured as follows:
TestResults
    Suite
        TestCase
            INotice (Error / Message)
see doc/TestResults.dia for more information
            
    
@date Feb 17, 2010
@author: Matthew A. Todd
'''
#import Suite
from BoostTestParser.Exception.NoneError import NoneError

class TestResults:
    '''
    Contains the entire results from a run of tests. Organized into suites.
    '''
    
    _suites = set([])

    def __init__(self):
        '''
        Constructor
        '''
    
    def addSuite(self,suite):
        if suite is None:
            raise NoneError("suite")
        # TODO: do we want isinstance?
        #if not isinstance(suite, Suite):
        #    raise TypeError("suite is not of type Suite")
        
        self._suites.add(suite)
        
    def getSuites(self):
        return self._suites
        
    def suiteCount(self):
        '''
        Returns the number of suites contained
        '''
        return len(self._suites)
        
        
    
