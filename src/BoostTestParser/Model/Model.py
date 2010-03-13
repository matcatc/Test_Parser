'''
Created on Mar 6, 2010

@author: matcat
'''
from BoostTestParser.Common import Observable
import copy

class Model(Observable.Observable):
    '''
    Model in MVC.
    
    Notifies observers whenever results changes (is assigned to).
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
           
    def parse(self):
        # TODO: which run?
        # how do we allow user to use particular runs?
        data = self.testRunner.runAll()
        self.results = self.parser.parseString(data.decode("utf-8"))
