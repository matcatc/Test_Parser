'''
@date Mar 22, 2010
@author Matthew A. Todd
'''

from ..Common import Observer

class Controller(Observer.Observer):
    '''
    Our common-basic controller.

    Doesn't do anything with updates.
    Doesn't use any threading.
    If we were to use threading, we'd have to make sure to
    spawn a non daemonic thread.
    @see BoostTestParser.Observable.Observable.notifyObservers()
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
    
    def run(self):
        '''
        Simply tells the model to parse
        
        @see Model.runAll()
        '''
        self.model.runAll()
        
