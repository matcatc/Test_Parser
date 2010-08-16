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

from TestParser.Common import Observer


class TextResultView(Observer.Observer):
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
            for infotype, data in result.getRelevantDisplayData():
                if infotype is not None and data is not None:
                    printData += "\t%s: %s" % (infotype, data)
                
            print("\t"*indentLevel + "%s: %s" % (result.type, printData))
            self._display(result, indentLevel+1 )