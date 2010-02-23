'''
Created on Feb 23, 2010

@author: matcat
'''

class NoneError(ValueError):
    '''
    classdocs
    '''
    _varName = ""


    def __init__(self, varName):
        '''
        Constructor
        '''
        self._varName = varName
        
    def toString(self):
        return "Error, " + self._varName + " is None"
        