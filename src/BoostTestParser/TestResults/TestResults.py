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
#from BoostTestParser.Exception.NoneError import NoneError

class TestResults:
    '''
    Contains the entire results from a run of tests. Organized into suites.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.suites = set([])
        
    def suiteCount(self):
        '''
        Returns the number of suites contained
        '''
        return len(self.suites)
        
        
    
