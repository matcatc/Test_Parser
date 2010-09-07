'''
@date Aug 28, 2010
@author Matthew Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

from .. import  Controller
from . import TkAbout

class TkViewController(Controller.Controller):
    '''
    Allows for windows to be closed in any order.
    
    Maintains a list of currently open windows. When all windows closed, root
    is destroyed. 
    
    @date Aug 28, 2010
    @author matcat
    '''
    
    def __init__(self, model, root):
        super().__init__(model)
        
        ## the tk root object
        self.root = root
        
        ## a list of Tk Toplevel items
        self.windows = []
        
    def addWindow(self, window):
        '''
        add a new Toplevel window to the list.
        
        Although accessor functions are non-pythonic, I don't want to go through
        a lot of trouble if we end up changing the windows data type.
        '''
        self.windows.append(window)
        
    def closeView(self, view):
        '''
        close the view.
        
        Removes view from observers. Destroys root if there are no more windows
        left open.
        
        @param view the view class object (TkResultView, TkStatisticView, etc.)
            We need to access its parent for the actual Toplevel window.
        '''
        self.model.removeObserver(view)
        view.parent.destroy()
        
        self.windows.remove(view.parent)
        if not self.windows:
            self.root.destroy()
    
    def displayAboutDialog(self, parent):
        TkAbout.TkAbout(parent)