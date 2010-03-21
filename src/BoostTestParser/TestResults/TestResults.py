class TestResults:
    '''
    Contains the entire results from a run of tests. Organized into suites.

    @verbatim
    Structured as follows:
    TestResults
        Suite
            TestCase
                Notice (Error / Message)
    @endverbatim
                
    @see TestResults.dia for more information  
                
        
    @date Feb 17, 2010
    @author Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.suites = set([])
        
    def suiteCount(self):
        '''
        @Return the number of suites contained
        '''
        return len(self.suites)
        
        
    
