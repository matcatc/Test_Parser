'''
Created on Feb 17, 2010

@author: matcat
'''

class Suite:
    '''
    classdocs
    '''

    testCases = set([])

    def __init__(self, testCases):
        '''
        Constructor
        '''
        self.testCases = set(testCases)
    
    def addTest(self, test):
        self.testCases.add(test)
        
    def testCount(self):
        '''
        Returns number of tests cases contained in this suite
        '''
        return len(self.testCases)
        