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
        
    def _display(self, results, indentLevel = 0):
        '''
        display the test results to stdout
        
        @pre results is of type TestComposite (or equivalent)
        
        @param results is TestComposite
        @param indentLevel is how many tabs to indent (how far down in levels
            we are
        '''
        for result in results.getChildren():
            printData = ""
            if(result.name is not None):
                printData += result.name
            if(result.timeTaken is not None):
                printData += "\ttime: " + str(result.timeTaken)
            if(result.file is not None):
                printData += "\tfile: " + result.file
            if(result.line is not None):
                printData += "\tline: " + str(result.line)
            if(result.info is not None):
                printData += "\tinfo: " + result.info
                
            print("\t"*indentLevel + result.type + ": " + printData)
            self._display(result, indentLevel+1 )
   

class TextViewController(Controller.Controller):
    '''
    A simple controller for TextView.
    
    Nothing to override
    @see Controller.Controller
    '''
        
