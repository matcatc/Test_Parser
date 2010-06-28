'''
@date Jun 28, 2010
@author matcat
'''
from .IRunner import IRunner

class PythonUnittestRunner(IRunner):
    '''
    Runner for Python Unittest framework.
    
    @warning Because of how Python Unittest is designed, we require
    that the test runner be setup a certain way. For parsing to work,
    we need the verbosity level to be set to 2. For running to work,
    we need the information all output to stdout. I.e: use the
    following command in your test runner.
    
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    
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
