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
    A simple view for our test runner / parser program.
    
    Simply displays the data to the console.
    Has indenting. Otherwise, basically the same as the output from
    Boost's test runner.
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
        @return test results
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
        print("\ttest: ", test.name)
        print("\t\t time: ", test.timeTaken)
        for notice in test.notices:
            self._displayNotice(notice)
            
    def _displayNotice(self, notice):
        print("\t\t", notice.type, "\tfile:", notice.file, "\tline:", notice.line, "\t", notice.info)
        

class TextViewController(Observer.Observer):
    '''
    A simple controller for TextView.
    
    Doesn't do anything with updates.
    Doesn't use any threading.
    If we were to use threading, we'd have to make sure to
    spawn a non daemonic thread.
    @see BoostTestParser.Observable.notifyObservers.__doc__
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
        pass
    
    def parse(self):
        '''
        TODO: think of better method name
        @see Model.parse
        
        Simply tells the model to parse
        '''
        self.model.run()
    

def main():
    '''
    Run the entire program using our TextView and its associated controller
    Will run tests, parse, display, and finally exit the program 
    '''
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
