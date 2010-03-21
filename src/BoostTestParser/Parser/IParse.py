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
        
    def parse(self, input):
        '''
        Delegates to _parseData()
        
        If a string is passed in, its a filename of a file to open for the data.
        If you want to pass in a string containing the actual xml data, use parseString()        
        @see parseString()
        @see _parseData()
        
        TODO: verify this works for possible input types
        
        @param input input to parse
        @return TestResults containing the parsed results
        '''
        tree = ET.parse(input)
        
        return self._parseData(tree)
    
    def parseString(self, input):
        '''
        Similar to parse(), except that works on a string with xml data in it.
        
        Delegates to _parseData()
        
        @see _parseData()
        @see parse
        @param input string containing the xml data
        @return TestResults containing the parsed results
        '''
        tree = ET.fromstring(input)
        return self._parseData(tree)
    
        
    def _parseData(self, tree):
        '''
        Is to be implemented in subclass
        
        @param tree an ElementTree with all of the xml data
        @return TestResults 
        '''
        raise NotImplementedError