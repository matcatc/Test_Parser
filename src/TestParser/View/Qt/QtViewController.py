'''
@date Aug 16, 2010
@author Matthew A. Todd
'''

from .. import Controller
from . import About

class QtViewController(Controller.Controller):
    '''
    A simple controller for QtResultView.
    
    Nothing to override
    @see Controller.Controller
    '''

    def displayAboutDialog(self):
        '''
        Displays the Qt based About Dialog
        '''
        widget = About.About()
        widget.exec()