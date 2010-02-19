'''
Created on Feb 19, 2010

@author: Matthew A. Todd
'''

class INotice():
    '''
    Interface for Errors and Message types.
    Used in TestCase. This way, a single list can hold
    Errors and Messages in the order they occurred.
    The other option would be to keep them separate,
    thereby loosing information (the order they occurred.)
    2/19/2010
    Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''
