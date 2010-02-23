'''
An entire suite of tests.

@date Feb 17, 2010
@author: Matthew A. Todd
'''
import TestCase
from BoostTestParser.Exception import NoneError

class Suite:
    '''
    Contains an entire suite of tests. Organized into test cases.
    '''

    _testCases = set([])

    def __init__(self):
        '''
        Constructor
        '''
    
    def addTest(self, test):
        if test is None:
            raise NoneError("test")
        if not isinstance(test, TestCase):
            raise TypeError("test is not of type TestCase")
        
        self._testCases.add(test)
        
    def getTestCases(self):
        return self._testCases
        
    def testCount(self):
        '''
        Returns number of tests cases contained in this suite
        '''
        return len(self._testCases)
        