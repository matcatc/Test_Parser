'''
@date Mar 6, 2010
@author: Matthew A. Tod
'''

from .UpdateJobPool import UpdateJobPool

class Observable(object):
    '''
    For observer pattern.
    
    Subclasses can be watched.
    This class defines all the methods and instance variables 
    necessary, so the subclass only needs to call __init__() and
    notifyObservers(), where appropriate.
    
    @date Mar 6, 2010
    @author Matthew A. Todd
    '''

    _NUMBER_THREADS = 2
    _updateJobPool = UpdateJobPool()

    def __init__(self):
        '''
        Constructor
        '''
        self.observers = set([])
        Observable._updateJobPool.createPool(Observable._NUMBER_THREADS)
        
    def registerObserver(self, observer):
        self.observers.add(observer)
    
    def removeObserver(self, observer):
        self.observers.discard(observer)
    
    def notifyObservers(self):
        '''
        uses a thread pool
        
        Won't return till all observers notified. This way we can ensure
        all the observer work is done before the program tries to quit.
        
        @warning this won't work if this code is being run in a daemonic
        thread as well.
        '''
        for observer in self.observers:
            Observable._updateJobPool.addJob(observer)
            
        # don't return until all jobs processed
        Observable._updateJobPool.waitUntilJobsFinished()
        