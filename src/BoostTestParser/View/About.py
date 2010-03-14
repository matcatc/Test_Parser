'''
Created on Mar 13, 2010

@author: matcat
'''

from PyQt4 import uic #@UnresolvedImport
from PyQt4 import QtGui #@UnresolvedImport
import sys

UiClass, WidgetClass = uic.loadUiType("./About.ui")


class About(UiClass, WidgetClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        WidgetClass.__init__(self)
        self.setupUi(self)
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    widget = About()
    widget.show()
    sys.exit(app.exec_())