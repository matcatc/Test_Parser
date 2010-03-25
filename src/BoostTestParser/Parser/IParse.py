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
    @author Matthew A. Todd 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def parse(self, file=None, stringData=None):
        '''
        Delegates to _parseData()
        @see _parseData()
        
        TODO: verify this works for possible input types
        
        @param stringData a string containing the xml data. If this is not None,
            then this will be used, regardless of what other data types are
            available.
        @param file a filename or file object.
        @return TestResults containing the parsed results
        '''
        if stringData is not None:
            tree = ET.fromstring(stringData)
            return self._parseData(tree)
        else:
            tree = ET.parse(file)
            return self._parseData(tree.getroot())
        
    def _parseData(self, tree):
        '''
        Is to be implemented in subclass
        
        @param tree an ElementTree with all of the xml data
        @return TestResults 
        '''
        raise NotImplementedError