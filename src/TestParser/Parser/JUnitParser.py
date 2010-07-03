'''
@date Jul 3, 2010
@author Matthew A. Todd
'''

from . import IParse
from TestParser.Common.Constants import Constants

import re

class JUnitParser(IParse.IParse):
    '''
    Parser for JUnit 3 and 4.
    
    @date Jul 3, 2010
    @author Matthew A. Todd
    '''


    def __init__(self, version):
        '''
        Constructor
        
        @param version version number of Junit (i.e: 3 or 4).
        '''
        self.version = version
    
    def parse(self, file=None, stringData=None):
        '''
        '''
        if stringData is not None:
            self._parseData(stringData)
        elif file is not None:
            self._parseData(file.read())
        else:
            #TODO: raise
            Constants.logger.error("ERROR: parse() needs data to parse")
            return
    
    
    def _parseData(self, stringData):
        '''
        statusLine contains the line of the following form:
        @verbatim
        ....E.F.E...
        @/endverbatim
        '''
        lines = stringData.split('\n')
        
        # If we're using JUnit 4, we need to remove the first line.
        if self.version == 4:
            lines.pop(0)
            
        statusLine = lines[0]
        
        # TODO: verify w/ RegEx?
        
        # FIX: returning wrong number.
        # see: http://docs.python.org/release/3.0.1/library/re.html#re.findall
        # mentions empty matches
        Constants.logger.debug("statusLine = " + statusLine)
        
        testCount = len(re.findall('.', statusLine))
        Constants.logger.debug("testCount = " + str(testCount))
        