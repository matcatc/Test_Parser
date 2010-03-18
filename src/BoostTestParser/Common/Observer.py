'''
@date Mar 6, 2010
@author: Matthew A. Todd
'''

class Observer(object):
    '''
    For observer pattern.
    
    Subclasses need to implement notify()
    
    @date Mar 6, 2010
    @author: Matthew A. Todd
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def notify(self):
        '''
        Subclasses need to implement this function.
        '''
        raise NotImplementedError
        