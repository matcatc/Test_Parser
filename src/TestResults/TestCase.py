'''
Created on Feb 17, 2010

@author: matcat
'''

class TestCase:
    '''
    issue: if messages and errors are stored in separate data structures,
    the individual order will be lost
    
    >>> testCase = TestCase()
    >>> testCase.hasError()
    False
        
    >>> testCase.addError(0)    # not real error type, but works for test
    >>> testCase.hasError()
    True
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
        
    def setTimeTaken(self, time):
        self.timeTaken = time
        
    def addError(self, error):
        self.errors.append(error)
        
    def addMessage(self, message):
        '''
        appends the error message to the list,
         so that the messages are kept in order
        '''
        self.messages.append(message)
        