'''
Created on Mar 6, 2010

@author: matcat
'''
from BoostTestParser.Common import Observable

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
        if results is not None:
            self.notifyObservers()
        self._results = results
    @results.deleter
    def results(self): #@DuplicatedSignature
        del self._results
        
    def parse(self):
        raise NotImplementedError
        #TODO: implement
        # get information to parse from testRunner
#        self.results = self.parser.parse()
