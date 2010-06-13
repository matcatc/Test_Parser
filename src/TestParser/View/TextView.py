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

from ..Common import Observer
from . import  Controller


class TextView(Observer.Observer):
    '''
    A simple view for our test runner / parser program.
    
    Simply displays the data to the console.
    Has indenting. Otherwise, basically the same as the output from
    Boost's test runner.
    '''
    
    @staticmethod
    def startView(model):
        '''
        Run the entire program using our TextView and its associated controller
        Will run tests, parse, display, and finally exit the program
        
        TODO: now that its a static method, will there be problems if we run
         it more than once?
        
        @see main.main()
        '''   
        # setup view and controller
        view = TextView(model)
        controller = TextViewController(model)
    
        # run (and implicitly display)
        controller.run()

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
        
        display() automatically pulls results, so we can just rely on display()
        '''
        self.display()
        
    def display(self):
        '''
        pulls latest information and displays it.
        
        delegates to _display() for displaying
        '''
        results = self._retrieveTestResults()
        if results is None:
            print("No test results to display")
            return
        self._display(results)
        
    def _display(self, results):
        '''
        display the test results to stdout
        
        @pre results is of type TestResults (or equivalent)
        '''
        for suite in results.suites:
            self._displaySuite(suite)
            
    def _displaySuite(self, suite):
        '''
        @pre suite is of type Suite (or equivalent)
        '''
        print("suite: ", suite.name)
        for test in suite.testCases:
            self._displayTest(test)
            
    def _displayTest(self, test):
        '''
        @pre test is of type Test (or equivalent)
        '''
        print("\ttest: ", test.name)
        print("\t\t time: ", test.timeTaken)
        for notice in test.notices:
            self._displayNotice(notice)
            
    def _displayNotice(self, notice):
        '''
        @pre notice is of type Notice (or equivalent)
        '''
        print("\t\t", notice.type, "\tfile:", notice.file, "\tline:", notice.line, "\t", notice.info)
        

class TextViewController(Controller.Controller):
    '''
    A simple controller for TextView.
    
    Nothing to override
    @see Controller.Controller
    '''
        
