'''
Created on Feb 19, 2010

@author: Matthew A. Todd
'''
import INotice

class Message(INotice):
    '''
    contains a simple string message.
    @see INotice
    '''

    _message = ""
    
    def __init__(self, message):
        '''
        Constructor
        
        message is a string.
        message can be empty, but it will raise a warning
        '''
        if message is None:
            raise ValueError("message is None")
        if message is "":
            raise Warning("message is empty")
        
        self._msg = message
        
        
    def getMessage(self):
        return self._message