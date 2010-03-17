'''
An entire suite of tests.

@date Feb 17, 2010
@author: Matthew A. Todd
'''

class Suite:
    '''
    Contains an entire suite of tests. Organized into test cases.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.testCases = set([])
        self.name = ""
        
    def testCount(self):
        '''
        Returns number of tests cases contained in this suite
        '''
        return len(self.testCases)
        