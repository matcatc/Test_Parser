

class Suite:
    '''
    Contains an entire suite of tests. Organized into test cases.
    

    @date Feb 17, 2010
    @author Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.testCases = set([])
        self.name = ""
        
    def testCount(self):
        '''
        Number of tests cases contained in this suite
        @return number of tests contained in suite.
        '''
        return len(self.testCases)
        
