'''
@author: Matthew A. Todd

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

from PyQt4 import uic #@UnresolvedImport
from PyQt4 import QtGui #@UnresolvedImport
from TestParser.Common.computeDataFilepath import computeDataFilepath
import sys


UiClass, WidgetClass = uic.loadUiType(computeDataFilepath("./About.ui", __file__))


class About(UiClass, WidgetClass):
    '''
    About box.

    @date Mar 13, 2010
    @author Matthew A. Todd
    '''

    def __init__(self):
        '''
        Constructor
        '''
        WidgetClass.__init__(self)
        self.setupUi(self)
        
        

def main():
    '''
    Way to run the about box for testing.
    '''
    app = QtGui.QApplication(sys.argv)
    widget = About()
    widget.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()