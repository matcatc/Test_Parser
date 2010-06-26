'''
@date Mar 12, 2010
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
import sys
from TestParser.Common.computeDataFilepath import computeDataFilepath

from . import Controller
from . import About

filename = "MainWindow.ui"

UiClass, WidgetClass = uic.loadUiType(computeDataFilepath(filename, __file__))

class QtView(UiClass, WidgetClass):
    '''
    Main window for our Qt implemented view.
    '''

    _red = QtGui.QColor("red")
    _green = QtGui.QColor("green")
    _white = QtGui.QColor("white")
    
    _redBrush = QtGui.QBrush(_red)
    _greenBrush = QtGui.QBrush(_green)
    _whiteBrush = QtGui.QBrush(_white)
    
    DEFAULT_BRUSH = _whiteBrush
    
    
    colorBrushes = {'error' : _redBrush,
                    'message' : _greenBrush,
                    'Suite' : _greenBrush,
                    'TestParser': _greenBrush,
                    'TestCase' : _greenBrush}
    
    TYPE_COL = 0
    NAME_COL = 1
    FILE_COL = 2
    LINE_COL = 3
    INFO_COL = 4
    TIME_COL = 4

    @staticmethod
    def startView(model):
        '''
        Run the qt view based program.
        
        @see main.main()
        '''
        # setup view
        app = QtGui.QApplication(sys.argv)
        widget = QtView(model)
        widget.show()

        # setup controller
        controller = QtViewController(model)

        # run
        controller.run()
        sys.exit(app.exec_())


    def __init__(self, model):
        '''
        Constructor
        '''
        WidgetClass.__init__(self)
        self.setupUi(self)

        self.model = model
        self.model.registerObserver(self)

        self.run = False

    def aboutDialog(self):
        '''
        Menu Cmd. Display about dialog.
        
        Modal.
        @date Jun 17, 2010
        '''
        widget = About.About()
        widget.exec()

    def reRun(self):
        '''
        Menu Cmd. Rerun previous test configuration.
        
        @date Jun 17, 2010
        '''
        self.model.runPrevious()


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
        self._updateTreeWidget(self._retrieveTestResults())

    def _clearTreeWidget(self):
        '''
        Clear out the TreeWidget.
        
        We have this function b/c treeWidget.clear() has some nasty side
        effects (seg-fault.) So we simply remove all the items and
        delete them by hand. We let the gc do all the clean up work.
        
        @date Jun 18, 2010
        '''
        while(self.treeWidget.takeTopLevelItem(0) is not None):
            pass


    def _updateTreeWidget(self, results):
        '''
        Actually update the GUI treeView widget
        '''

        self._clearTreeWidget()
        tree = self.treeWidget
        
        self._displayResults(tree, results)


    def _displayResults(self, parent, result):
        '''
        @param parent is the parent item in the tree
        @param results results is all the Test Results data we want to 
            display below given parent item
            
        @return returns Brush if a particular brush/color should work
            its way up (eg: we had an error, therefore error's color
            should work its way up)
        
        @date Jun 23, 2010
        '''
        numCols = self.treeWidget.columnCount()
        
        resultItem = QtGui.QTreeWidgetItem(parent)
        
        resultItem.setText(QtView.TYPE_COL, result.type)
        
        # parse and display data
        for infotype, data in result.getRelevantDisplayData():
            if infotype == "name":
                resultItem.setText(QtView.NAME_COL, data)
            elif infotype == "file":
                resultItem.setText(QtView.FILE_COL, data)
            elif infotype == "line":
                resultItem.setText(QtView.LINE_COL, data)
            elif infotype == "info":
                resultItem.setText(QtView.INFO_COL, data)
            elif infotype == "time":
                resultItem.setText(QtView.TIME_COL, "time: " + data)

        retBrush = None
        for child in result.getChildren():
            temp = self._displayResults(resultItem, child)
            if temp is not None:
                retBrush = temp

        try:
            brush = QtView.colorBrushes[result.type]
        except KeyError:
            brush = QtView.DEFAULT_BRUSH

        if result.type == "error":
            self._colorRow(resultItem, numCols, brush)
            return brush
        elif retBrush is not None:
            self._colorRow(resultItem, numCols, retBrush)
            return retBrush
        else:
            self._colorRow(resultItem, numCols, brush)
            return None
        
    def _colorRow(self, item, numCols, brush):
        '''
        Colors a given item across all cols (the entire row)
        with the given brush.
        
        @date Jun 23, 2010
        '''
        for i in range(numCols):
            item.setBackground(i, brush)
        

class QtViewController(Controller.Controller):
    '''
    A simple controller for QtView.
    
    Nothing to override
    @see Controller.Controller
    '''


