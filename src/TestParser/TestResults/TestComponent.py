'''
@date Jun 23, 2010
@author Matthew A. Todd
'''

class TestComponent(object):
    '''
    Abstract class for Test Results Composite pattern.
    
    Currently we have to set variables that could be set to None here,
    so that we don't get attribute errors.
    TODO: find better solution
    
    @date Jun 23, 2010
    @author Matthew A. Todd
    '''


    def __init__(self, type):
        '''
        Constructor
        '''
        self.type = type
        self.name = None
        self.timeTaken = None
        self.file = None
        self.line = None
        self.info = None
        
    def getChildren(self):
        '''
        Get all children/composed items.
        
        To be implemented in subclasses.
        '''
        raise NotImplementedError