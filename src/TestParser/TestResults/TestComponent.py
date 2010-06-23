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
        
    def getChildren(self):
        '''
        Get all children/composed items.
        
        To be implemented in subclasses.
        '''
        raise NotImplementedError
    
    def getRelevantDisplayData(self):
        '''
        Returns all the data to be displayed as a list of tuples: (infotype, data)
        where infotype is line, file, name, etc.
        '''
        raise NotImplementedError