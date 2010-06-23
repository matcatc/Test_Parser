'''
@date Jun 23, 2010
@author Matthew A. Todd
'''

class TestComponent(object):
    '''
    Abstract class for Test Results Composite pattern.
    
    @date Jun 23, 2010
    @author Matthew A. Todd
    '''


    def __init__(self, type):
        '''
        Constructor
        '''
        self.type = type
        
    def getChildren(self):
        '''
        Get all children/composed items.
        
        To be implemented in subclasses.
        '''
        raise NotImplementedError