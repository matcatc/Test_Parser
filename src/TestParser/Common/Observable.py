'''
@date Mar 6, 2010
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

from .UpdateJobPool import UpdateJobPool
from .Constants import Constants

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
        self._observers = set([])
        
        if Constants.threading:
            Observable._updateJobPool.createPool(Observable._NUMBER_THREADS)
        
    def registerObserver(self, observer):
        self._observers.add(observer)
    
    def removeObserver(self, observer):
        self._observers.discard(observer)
    
    def notifyObservers(self):
        if Constants.threading:
            self._notifyObservers_threaded()
        else:
            self._notifyObservers_unthreaded()
    
    def _notifyObservers_unthreaded(self):
        for observer in self._observers:
            observer.update()
    
    def _notifyObservers_threaded(self):
        '''
        uses a thread pool
        
        Won't return till all observers notified. This way we can ensure
        all the observer work is done before the program tries to quit
        (provided the running thread is not daemonic.)
        
        @warning this won't work if this code is being run in a daemonic
        thread as well.
        '''
        for observer in self._observers:
            Observable._updateJobPool.addJob(observer)
            
        # don't return until all jobs processed
        Observable._updateJobPool.waitUntilJobsFinished()
        