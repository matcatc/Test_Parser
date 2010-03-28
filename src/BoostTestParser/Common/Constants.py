'''
@date Mar 28, 2010
@author Matthew A. Todd
'''

import sys

class Constants_class(object):
    '''
    contains project wide constants.
    
    Singleton pattern. Everyone should use static variable Constants, defined
    later in this module.
    
    errStream: error stream
     This way programs can use the error/warning that would be otherwise
     output strait to the console. Also very useful for testing purposes.
    
    @date Mar 28, 2010
    @author Matthew A. Todd
    '''
    
    def __init__(self):
        '''
        '''
        self.reset()
    
    def reset(self):
        '''
        reset all the values to their default values
        '''
        self.errStream = sys.stderr
        
        
Constants = Constants_class()