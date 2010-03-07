'''
@date Feb 22, 2010
@author: Matthew A. Todd
'''
from xml.etree import ElementTree as ET

class IParse():
    '''
    Parsing interface.
    A strategy.
    
    Classes that implement this interface are to parse XML and return a TestResults (import TestResults).
    They do so by implementing _parseData().
    
    @date Feb 22, 2010
    @author: Matthew A. Todd 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def parse(self, input):
        '''
        delegates to _parseData(), which is to be implemented in a subclass.
        
        @param input: input to parse
        # TODO: verify this works for possible input types
        '''
        tree = ET.parse(input)
        
        return self._parseData(tree)
        
    def _parseData(self, tree):
        '''        
        @return TestResults
        @param tree: an ElementTree with all of the xml data 
        '''
        raise NotImplementedError