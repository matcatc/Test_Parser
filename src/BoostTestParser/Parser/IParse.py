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
        
        @param input: input can be of type string or a file
         If its a string, it contains all of the data (i.e: its not a filename)
        '''
        tree = None
        
        if isinstance(input, file):
            tree = ET.parse(input)
        elif isinstance(input, str):
            tree = ET.fromstring(input)
        else:
            raise TypeError("trying to parse unknown type")
        
        return self._parseData(tree)
        
    def _parseData(self, tree):
        '''        
        @return TestResults
        @param tree: an ElementTree with all of the xml data 
        '''
        raise NotImplementedError