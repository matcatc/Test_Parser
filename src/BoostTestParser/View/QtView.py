'''
@date Mar 12, 2010
@author: Matthew A. Todd
'''

from PyQt4 import uic #@UnresolvedImport
from PyQt4 import QtGui #@UnresolvedImport
import sys

from ..Model import Model
from ..Parser import BasicParser
from ..Model import TestRunner
from ..Common import Observer

UiClass, WidgetClass = uic.loadUiType("./BoostTestParser/View/MainWindow.ui")

class QtView(UiClass, WidgetClass):
    '''
    Main window for our Qt implemented view.
    '''

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
        


class QtViewController(Observer.Observer):
    '''
    A simple controller for QtView.
    
    Doesn't do anything with updates.
    Doesn't use any threading.
    If we were to use threading, we'd have to make sure to
    spawn a non daemonic thread.
    @see BoostTestParser.Observable.notifyObservers()
    
    TODO: do we need this controller?
    
    TODO: create controller parent class
     this was a copy and past of TextViewController
    '''
    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.model.registerObserver(self)
    
    def update(self):
        '''
        Nothing for our controller to do when model updates us
        '''
        print("Updating QtViewController")
    
    def run(self):
        '''        
        Simply tells the model to parse
        
        @see Model.runAll()
        '''
        self.model.runAll()
        
def qtViewMain(model):
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