'''
Created on Mar 6, 2010

@author: matcat
'''
from ..Common import Observable
import copy, threading
import sys

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
        lock = threading.Lock()
        with lock:
                data = self.testRunner.runAll()
                self._doParse(data)

    # TODO: other runs (as needed)
