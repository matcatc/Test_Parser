

from PyQt4 import uic #@UnresolvedImport
from PyQt4 import QtGui #@UnresolvedImport
import sys

UiClass, WidgetClass = uic.loadUiType("./About.ui")


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