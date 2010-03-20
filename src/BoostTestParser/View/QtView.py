'''
Created on Mar 12, 2010

@author: matcat
'''

from PyQt4 import uic #@UnresolvedImport
from PyQt4 import QtGui #@UnresolvedImport
from PyQt4 import QtCore
import sys

from ..Model import Model
from ..Parser import BasicParser
from ..Model import TestRunner
from ..Common import Observer

UiClass, WidgetClass = uic.loadUiType("./BoostTestParser/View/MainWindow.ui")

class QtView(UiClass, WidgetClass):
    '''
    classdocs
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
    @see BoostTestParser.Observable.notifyObservers.__doc__
    
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
        @see Model.runAll()
        
        Simply tells the model to parse
        '''
        self.model.runAll()


def main():
    if len(sys.argv) < 2:
        print("Usage: test parser <test_runner>")
        return
    
    # setup model
    model = Model.Model()
    runner = TestRunner.TestRunner()
    runner.runner = sys.argv[1]
    model.testRunner = runner
    model.parser = BasicParser.BasicParser()
    
    # setup view
    app = QtGui.QApplication(sys.argv)
    widget = QtView(model)
    widget.show()
    
    # setup controller
    controller = QtViewController(model)
    
    # run
    controller.run()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()