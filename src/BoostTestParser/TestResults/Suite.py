'''
An entire suite of tests.

@date Feb 17, 2010
@author: Matthew A. Todd
'''
#import TestCase
from BoostTestParser.Exception.NoneError import NoneError

class Suite:
    '''
    Contains an entire suite of tests. Organized into test cases.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._testCases = set([])
        self._name = ""

        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    def addTest(self, test):
        if test is None:
            raise NoneError("test")
        # TODO: do we want this isinstance? 
        #if not isinstance(test, TestCase.TestCase):
        #    raise TypeError("test is not of type TestCase")
        
        self._testCases.add(test)
        #self._testCases.append(test)
        
    def getTestCases(self):
        return self._testCases
        
    def testCount(self):
        '''
        Returns number of tests cases contained in this suite
        '''
        return len(self._testCases)
        