'''
@date Apr 17, 2010
@author Matthew A. Todd
'''
import queue, threading



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
        ## TODO restrict access to jobQueue
        #  property: read only
        #  or make private and provide helper function for join()
        self.jobQueue = queue.Queue(0)
    
        self._bPoolCreated = False
        
        self._threadCount = 0
        ## number of threads to be removed
        self._removeCount = 0

    
    def createPool(self, numThreads):
        '''
        Creates the initial pool of threads.
        If called more than once, it doesn't do anything subsequent times.
        '''
        if not self._bPoolCreated:
            print("creating thread pool")
            self._bPoolCreated = True
            self.addThreads(numThreads)


    def addThreads(self, numThreads):
        '''
        Add threads to those currently running.
        '''
        if self._bPoolCreated == False:
            # TODO: raise
            print("cannot add threads to a job pool that hasn't been created")
            return
        
        print("adding threads:", numThreads)
        for x in range(numThreads):
            self._threadCount += 1
            thread = UpdateThread(self)
            thread.daemon = True
            thread.start()

    def removeThreads(self, numThreads):
        '''
        Removes threads from those that are currently running.

        Works by having threads check to see if they should die off after they're done
        with a job. This way we don't interupt any work that is occuring.
        '''
        self._removeCount += numThreads
        
    def addJob(self, observer):
        '''
        add a job to the jobQueue
        '''
        self.jobQueue.put(observer)
        
        
        

class UpdateThread (threading.Thread):
    '''   
    worker thread that updates observers.
    
    To only be used by UpdateThreadPool.
    @see UpdateJobPool
    
    @date Mar 14, 2010
    @author Matthew A. Todd
    '''
    def __init__ (self, jobPool):
        threading.Thread.__init__(self)
        self.jobPool = jobPool
        pass

    def _dieOff(self):
        '''
        Compute whether calling thread should die off.
        
        @warning requires that client function actually kills the thread (itself).
        
        @return True if thread should die off.
        '''
        if self.jobPool._removeCount > 0:
            self.jobPool._removeCount -= 1
            return True
        return False


    def run (self):
        '''
        Actual work is done here. Gets job (observer) from queue,
        and calls update on it. 
        
        will only return (die off) if _removeCount > 0
        '''
        while True:
            observer = self.jobPool.jobQueue.get()

            # job processing
            if observer != None:
                observer.update()
            else:
                print("cannot process non-existent observer")

            # notify queue that job is done
            self.jobPool.jobQueue.task_done()

            # die off here
            lock = threading.Lock()
            with lock:
                if self._dieOff():
                    print("Removing thread")
                    return