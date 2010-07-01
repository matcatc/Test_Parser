'''
@date Mar 6, 2010
@author Matthew A. Todd

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
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>
'''

from ..Common import Observable
import copy, threading

class Model(Observable.Observable):
    '''
    Model in MVC.
    
    TODO: None issues
    Test Runner and Parser need to be set before calling methods.
    If they are None, and need to be used, there are two possibilities,
    based on how I end up implementing.
    1) testResults set to None or not changed, which doesn't result in
        an observer notification being sent out. I.e: Model lies silent.
    2) an exception is thrown notifying the client that the method failed.
        Not sure what exception should be thrown. Might just rethrow
        original None exception.
    
    Notifies observers whenever results changes (is assigned to).
    @see results.setter
    
    Data contained:
        test runner
        test results
        parser
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Model, self).__init__()
        self.results = None
        self.testRunner = None
        self.parser = None
        self._runLock = threading.Lock()
    
    @property
    def results(self):
        return self._results
    @results.setter
    def results(self, results): #@DuplicatedSignature
        '''
        Notify observers that results has changed.
        Will not notify if new value is None.
        '''
        self._results = copy.deepcopy(results)
        if results is not None:
            self.notifyObservers()
    @results.deleter
    def results(self): #@DuplicatedSignature
        del self._results
        
    def _doParse(self, data):
        '''
        TODO: What if parser is None?
        Currently, if parser is None, an AttributeError will be thrown by
        trying to access parse()
        
        @throws AttributeError when parser is None
        '''
        
        try:
            decodedData = data.decode("utf-8")
        except AttributeError:
            decodedData = data
        
        self.results = self.parser.parse(stringData=decodedData)
           
    def runAll(self):
        '''
        Runs all tests available in testRunner
        
        TODO: what if testRunner is None?
        Currently, if testRunner is None, an AttributeError will be thrown
        by trying to access runAll()
        
        @throws AttributeError when testRunner is None
        
        We should keep lock.
        We should lock this function (should we?)
        b/c it runs an algorithm before assigning
        Plus we have to worry about messing w/ data.
        We could always make data a thread local variable,
        but I think locking the entire function seems reasonable.
        '''
        with self._runLock:
            data = self.testRunner.runAll()
            self._doParse(data)

    def runPrevious(self):
        '''
        Tells testRunner to rerun using previous configuration
        
        @see TestRunner.runPrevious()
        '''
        with self._runLock:
            data = self.testRunner.runPrevious()
            self._doParse(data)
