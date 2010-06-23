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

    red = QtGui.QColor("red")
    green = QtGui.QColor("green")
    redBrush = QtGui.QBrush(red)
    greenBrush = QtGui.QBrush(green)

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
        
        TODO: consider using a dictionary for colors. That we can just
        change the dictionary to change colors.
        '''

        self._clearTreeWidget()
        tree = self.treeWidget
        
        self._displayResults(tree, results)


    def _displayResults(self, parent, result):
        '''
        @param parent is the parent item in the tree
        @param results results is all the Test Results data we want to 
            display below given parent item
        @return returns True if parent should be Red
        
        @date Jun 23, 2010
        '''
        TYPE = 0
        NAME = 1
        FILE = 2
        LINE = 3
        INFO = 4
        TIME = 4
        numCols = self.treeWidget.columnCount()
        
        resultItem = QtGui.QTreeWidgetItem(parent)
        
        resultItem.setText(TYPE, result.type)
        
        for infotype, data in result.getRelevantDisplayData():
            if infotype == "name":
                resultItem.setText(NAME, data)
            elif infotype == "file":
                resultItem.setText(FILE, data)
            elif infotype == "line":
                resultItem.setText(LINE, data)
            elif infotype == "info":
                resultItem.setText(INFO, data)
            elif infotype == "time":
                resultItem.setText(TIME, "time: " + data)

        bRedChild = False
        for child in result.getChildren():
            if self._displayResults(resultItem, child) == True:
                bRedChild = True

        # if this is an error or we have a red colored child
        if result.type == "error" or bRedChild == True:
            self._colorRow(resultItem, numCols, QtView.redBrush)
            return True
        else:
            self._colorRow(resultItem, numCols, QtView.greenBrush)
            return False
        
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


