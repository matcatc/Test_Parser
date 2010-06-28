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
        