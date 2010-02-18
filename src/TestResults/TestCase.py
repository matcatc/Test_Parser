'''
Created on Feb 17, 2010

@author: matcat
'''

class TestCase:
    '''
    issue: if messages and errors are stored in separate data structures,
    the individual order will be lost
    '''

    errors = ([])
    timeTaken = 0
    messages = []

    def __init__(self):
        '''
        Constructor
        '''
    
    def hasError(self):
        if len(self.errors) > 0:
            return True
        else:
            return False
        
    def addError(self, error):
        self.errors.add(error)
        
    def addMessage(self, message):
        '''
        appends the error message to the list, so that the messages are kept in order
        '''
        self.messages.append(message)
        