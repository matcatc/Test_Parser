'''
@date Jul 4, 2010
@author matcat
'''

from .IRunner import IRunner

class JUnitRunner(IRunner):
    '''
    classdocs
    @date Jul 4, 2010
    @author matcat
    '''


    def __init__(self):
        '''
        Constructor
        
        we're leaving it up to the user to use the (correct)
        JUnit test runner, then we don't need to know version information
        here.
        '''
        super().__init__()
    
    
    def computeCmd(self, params):
        '''
        Just run w/o any paramaters
        '''
        return self.runner