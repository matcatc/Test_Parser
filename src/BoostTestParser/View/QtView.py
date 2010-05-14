'''
@date Mar 12, 2010
@author: Matthew A. Todd
'''

from PyQt4 import uic #@UnresolvedImport
from PyQt4 import QtGui #@UnresolvedImport
import sys

from . import Controller

UiClass, WidgetClass = uic.loadUiType("./BoostTestParser/View/MainWindow.ui")

class QtView(UiClass, WidgetClass):
    '''
    Main window for our Qt implemented view.
    '''
    
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
        print("Updating QtView")
        self._updateTreeWidget(self._retrieveTestResults())
        
    def _updateTreeWidget(self, results):
        '''
        Actually updated the GUI treeView widget
        
        TODO: finish implementing
        '''
        tree = self.treeWidget
        tree.clear()
        
        # suite name is null for some reason
        for suite in results.suites:
            print ("suite name =", suite.name)
            suiteItem = QtGui.QTreeWidgetItem(suite.name)
            for test in suite.testCases:
                pass
            tree.addTopLevelItem(suiteItem)
        


class QtViewController(Controller.Controller):
    '''
    A simple controller for QtView.
    
    Nothing to override
    @see Controller.Controller
    '''
        

