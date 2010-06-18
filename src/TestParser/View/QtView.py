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
        '''

        self._clearTreeWidget()
        tree = self.treeWidget

        numCols = tree.columnCount()

        for suite in results.suites:
            suiteItem = QtGui.QTreeWidgetItem(tree)
            suiteItem.setText(0, "Suite")
            suiteItem.setText(1, suite.name)

            for i in range(numCols):
                suiteItem.setBackground(i, QtView.greenBrush)

            for test in suite.testCases:
                testItem = QtGui.QTreeWidgetItem(suiteItem)
                testItem.setText(0, "Test")
                testItem.setText(1, test.name)

                for i in range(numCols):
                    testItem.setBackground(i, QtView.greenBrush)

                for notice in test.notices:
                    noticeItem = QtGui.QTreeWidgetItem(testItem)
                    noticeItem.setText(0, notice.type)
                    noticeItem.setText(2, notice.file)
                    noticeItem.setText(3, str(notice.line))
                    noticeItem.setText(4, notice.info)

                    # TODO: this is somewhat hardcoded
                    #  better: static/const list of items to color red
                    if notice.type == "error":
                        for i in range(numCols):
                            noticeItem.setBackground(i, QtView.redBrush)
                            testItem.setBackground(i, QtView.redBrush)
                            suiteItem.setBackground(i, QtView.redBrush)
                    else:
                        for i in range(numCols):
                            noticeItem.setBackground(i, QtView.greenBrush)


class QtViewController(Controller.Controller):
    '''
    A simple controller for QtView.
    
    Nothing to override
    @see Controller.Controller
    '''


