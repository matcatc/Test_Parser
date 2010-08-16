'''
@date Aug 16, 2010
@author matcat
'''

from .. import  Controller

class TextViewController(Controller.Controller):
    '''
    A simple controller for TextResultView.
    
    Because all/most of the text views don't need to override
    anything, we're going to just have one main controller for all
    text based views.
    
    Nothing to override
    @see Controller.Controller
    '''