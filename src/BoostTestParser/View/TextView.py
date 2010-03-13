'''
Created on Mar 12, 2010

@author: matcat
'''

from BoostTestParser.Model import Model
from BoostTestParser.Parser import BasicParser
from BoostTestParser.Model import TestRunner
from BoostTestParser.Common import Observer
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
        print("test: ", test.name)
        print("time: ", test.timeTaken)
        for notice in test.notices:
            self._displayNotice(notice)
            
    def _displayNotice(self, notice):
        print(notice.type, "file: ", notice.file, "line: ", notice.line, notice.info)
        

def main():
    model = Model.Model()
    runner = TestRunner.TestRunner()
    if len(sys.argv) < 2:
        print("Usage: test parser <test_runner>")
        return
    runner.runner = sys.argv[1]
    model.testRunner = runner
    model.parser = BasicParser.BasicParser()
    view = TextView(model)
    model.parse()
    view.display()
    
if __name__ == "__main__":
    main()
