'''
Created on Mar 12, 2010

@author: matcat
'''

from ..Model import Model
from ..Parser import BasicParser
from ..Model import TestRunner
from ..Common import Observer
import sys

class TextView(Observer.Observer):
    '''
    classdocs
    '''

    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.model.registerObserver(self)
        
    def _retrieveTestResults(self):
        '''
        get the test results from the model
        '''
        return self.model.results
    
    def update(self):
        '''
        For observer.
        
        display automatically pulls results, so we can just rely on display
        '''
        print("updating TextView")
        self.display()
        
    def display(self):
        results = self._retrieveTestResults()
        if results is None:
            print("No test results to display")
            return
        self._display(results)
        
    def _display(self, results):
        '''
        display the test results to stdout
        '''
        for suite in results.suites:
            self._displaySuite(suite)
            
    def _displaySuite(self, suite):
        print("suite: ", suite.name)
        for test in suite.testCases:
            self._displayTest(test)
            
    def _displayTest(self, test):
        print("\ttest: ", test.name)
        print("\t\t time: ", test.timeTaken)
        for notice in test.notices:
            self._displayNotice(notice)
            
    def _displayNotice(self, notice):
        print("\t\t", notice.type, "\tfile:", notice.file, "\tline:", notice.line, "\t", notice.info)
        

class TextViewController(Observer.Observer):
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
        pass
    
    def parse(self):
        '''
        TODO: think of better method name
        
        Simply tells the model to parse
        '''
        self.model.parse()
    

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
    
    # setup view and controller
    view = TextView(model)
    controller = TextViewController(model)

    # parse (and implicitly display)
    controller.parse()
    
if __name__ == "__main__":
    main()
