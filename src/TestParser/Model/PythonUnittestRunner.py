'''
@date Jun 28, 2010
@author matcat
'''
from .IRunner import IRunner

class PythonUnittestRunner(IRunner):
    '''
    Runner for Python Unittest framework.
    
    @date Jun 28, 2010
    @author matcat
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
    
    
    def computeCmd(self, params):
        '''
        Just run w/o any paramaters
        '''
        return [self.runner]
