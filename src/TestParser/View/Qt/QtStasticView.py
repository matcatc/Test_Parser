'''
@date Aug 16, 2010
@author Matthew Todd
'''

import sys
from TestParser.Common import ComputeStatistics

try:
    from PyQt4 import uic #@UnresolvedImport
    from PyQt4 import QtGui #@UnresolvedImport
except:
    sys.exit("Failed to import PyQt4. QtResultView needs PyQt4 in order to function. Please install PyQt4 or choose another UI.")

from TestParser.Common.computeDataFilepath import computeDataFilepath

filename = "Statistic.ui"

UiClass, WidgetClass = uic.loadUiType(computeDataFilepath(filename, __file__))

class QtStatisticView(UiClass, WidgetClass):
    def __init__(self, model, controller):
        '''
        Constructor
        '''
        WidgetClass.__init__(self)
        self.setupUi(self)

        self.model = model
        self.model.registerObserver(self)

        self.controller = controller
        

        green = QtGui.QColor("green")
        passColor = QtGui.QPalette()
        passColor.setColor(QtGui.QPalette.Foreground, green)
        self.PassDisplay.setPalette(passColor)

        red = QtGui.QColor("red")
        errorColor = QtGui.QPalette()
        errorColor.setColor(QtGui.QPalette.Foreground, red)
        self.FailDisplay.setPalette(errorColor)
        self.ErrorDisplay.setPalette(errorColor)


    def aboutDialog(self):
        self.controller.displayAboutDialog()
        
    def _retrieveTestResults(self):
        '''
        get the test results from the model
        @return test results
        '''
        return self.model.results

    def update(self):
        '''
        For observer.
        '''
        self._display(self._retrieveTestResults())
        
    def _display(self, results):
        passes, fails, errors = ComputeStatistics.computeStatistics(results)
                
        self.PassDisplay.display(passes)
        self.FailDisplay.display(fails)
        self.ErrorDisplay.display(errors)