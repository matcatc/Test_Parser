'''
@date Aug 16, 2010
@author Matthew A. Todd

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

from .. import Controller
from . import About
import sys

try:
    from PyQt4 import QtGui #@UnresolvedImport
except:
    sys.exit("Failed to import PyQt4. QtResultView needs PyQt4 in order to function. Please install PyQt4 or choose another UI.")

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
        
    def reportException(self, e):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "", str(e))
        msgBox.exec();