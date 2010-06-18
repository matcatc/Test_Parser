'''
@date Apr 17, 2010
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
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''
import queue, threading
from TestParser.Common.Constants import Constants

class NonExistentJobPool_Exception(Exception):
    '''
    Exception. No JobPool in existence.
    
    There are no threads currently running to process jobs.
    
    TODO: anything to implement?
    '''
    pass

class UpdateJobPool(object):
    '''
    Job is to update a given target. So jobQueue contains observers.
    
    @see UpdateThread
    @date Apr 17, 2010
    @author Matthew A. Todd
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._jobQueue = queue.Queue(0)

        self._bPoolCreated = False

        self._threadCount = 0
        ## number of threads to be removed
        self._removeCount = 0


    def createPool(self, numThreads):
        '''
        Creates the initial pool of threads.
        If called more than once, it doesn't do anything subsequent times.
        
        @pre see addThreads() regarding numThreads
        '''
        if not self._bPoolCreated:
            print("creating thread pool", file=Constants.errStream)     # TODO: should be a log
            self._bPoolCreated = True
            self.addThreads(numThreads)


    def addThreads(self, numThreads):
        '''
        Add threads to those currently running.
        
        @pre numThreads >= 0. If negative,
            nothing will happen.
        '''
        if self._bPoolCreated == False:
            raise NonExistentJobPool_Exception("cannot add threads to a job pool that hasn't been created")

        print("adding threads:", numThreads, file=Constants.errStream)  # TODO: should be a log
        for x in range(numThreads):
            self._threadCount += 1
            thread = UpdateThread(self)
            thread.daemon = True
            thread.start()

    def removeThreads(self, numThreads):
        '''
        Removes threads from those that are currently running.

        Works by having threads check to see if they should die off after they're done
        with a job. This way we don't interrupt any work that is occurring.
        
        @pre numThreads >= 0. If negative, could have unexpected
            consequences.
        '''
        self._removeCount += numThreads

    def addJob(self, observer):
        '''
        add a job to the jobQueue
        '''
        self._jobQueue.put(observer)

    def waitUntilJobsFinished(self):
        '''
        wait until all the jobs are finished
        
        i.e: join()
        
        If there are no threads to run the jobs, this function will wait
        indefinitely. Although another thread may add threads, which COULD
        then allow this function to complete. If you want a version which
        will throw if there are no threads currently, use
        waitUntilJobsFinished_Raise().
        
        I'm not sure if its better to just call it join(), as that seems to
        be standard (threading.join() and queue.join().) But I don't like
        how ambiguous it is.
        
        @see waitUntilJobsFinished_Raise()
        @date Apr 23, 2010
        @author Matthew A. Todd
        '''
        self._jobQueue.join()

    def waitUntilJobsFinished_Raise(self):
        '''
        same as waitUntilJobsFinished(), but will raise an exception if there
        are not threads (in existence) to process jobs.

        @see waitUntilJobsFinished()        
        @throw NonExistentJobPool_Exception
        @date Apr 23, 2010
        @author Matthew A. Todd
        '''
        if self._threadCount == 0:
            raise NonExistentJobPool_Exception()

        self._jobQueue.join()


class UpdateThread (threading.Thread):
    '''   
    worker thread that updates observers.
    
    To only be used by UpdateThreadPool.
    Since its so closely intertwined with UpdateThreadPool, I'm going to allow
    it to access its private members instead of creating special functions.
    Since creating functions would expose the data to the entire world, when
    we just want this class to access it. If I can think of a good way to make
    this cleaner, I'll go ahead and do so.
    
    @see UpdateJobPool
    @date Mar 14, 2010
    @author Matthew A. Todd
    '''
    NON_EXISTENT_OBSERVER_MSG = "cannot process non-existent observer"

    def __init__ (self, jobPool):
        threading.Thread.__init__(self)
        self.jobPool = jobPool

    def _dieOff(self):
        '''
        Compute whether calling thread should die off.
        
        @warning requires that client function (run()) actually
        kills the thread (itself).
        
        @return True if thread should die off.
        '''
        if self.jobPool._removeCount > 0:
            self.jobPool._removeCount -= 1
            self.jobPool._threadCount -= 1
            return True
        return False


    def run (self):
        '''
        Actual work is done here. Gets job (observer) from queue,
        and calls update on it.
        
        Will print out an error message to Constants.errStream if
        a job is None.
        
        @see dieOff() for die off conditions
        '''
        while True:
            observer = self.jobPool._jobQueue.get()

            # job processing
            if observer != None:
                observer.update()
            else:
                print(UpdateThread.NON_EXISTENT_OBSERVER_MSG, file=Constants.errStream)

            # notify queue that job is done
            self.jobPool._jobQueue.task_done()

            # die off here
            lock = threading.Lock()
            with lock:
                if self._dieOff():
                    print("Removing thread")
                    return
