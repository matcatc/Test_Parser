'''
@date Aug 16, 2010
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
        self.PassLabel.setPalette(passColor)

        red = QtGui.QColor("red")
        errorColor = QtGui.QPalette()
        errorColor.setColor(QtGui.QPalette.Foreground, red)
        self.FailDisplay.setPalette(errorColor)
        self.FailLabel.setPalette(errorColor)
        self.ErrorDisplay.setPalette(errorColor)
        self.ErrorLabel.setPalette(errorColor)

        self.setWindowTitle("Test Parser Statistic - %s" % ' '.join(self.model.testRunner.runner)) #TODO: refactor


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