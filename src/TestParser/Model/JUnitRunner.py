'''
@date Jul 4, 2010
@author matcat
'''

from .IRunner import IRunner
from TestParser.Common.InvalidJUnitVersion import InvalidJUnitVersion

class JUnitRunner(IRunner):
    '''
    classdocs
    @date Jul 4, 2010
    @author matcat
    '''


    def __init__(self, version):
        '''
        Constructor
        
        @param version version number of Junit (i.e: 3 or 4).
        '''
        super().__init__()
        
        if version != 3 and version != 4:
            raise InvalidJUnitVersion()
        self.version = version
    
    
    def computeCmd(self, params):
        '''
        Just run w/o any paramaters
        '''
        return [self.runner]