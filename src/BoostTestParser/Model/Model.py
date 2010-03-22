'''
Created on Mar 6, 2010

@author: matcat
'''
from ..Common import Observable
import copy, threading

class Model(Observable.Observable):
    '''
    Model in MVC.
    
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
        Notify observers that results has changed. Will not notify if None.
        '''
        self._results = copy.deepcopy(results)
        if results is not None:
            self.notifyObservers()
    @results.deleter
    def results(self): #@DuplicatedSignature
        del self._results
        
    def _doParse(self, data):
        self.results = self.parser.parse(stringData=data.decode("utf-8"))
           
    def runAll(self):
        '''
        Runs all tests avaiable in testRunner
        
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
