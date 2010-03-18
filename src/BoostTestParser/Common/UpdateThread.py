'''
Created on Mar 14, 2010

@author: matcat
'''
import threading, queue

class UpdateThread (threading.Thread):
    '''
    Job is to update a given target. So jobPool contains observers.
    '''
    # Note that these are static variables
    
    # TODO restrict access to jobPool
    #  property: read only
    #  or make private and provide helper function for join()
    jobPool = queue.Queue(0)

    _bPoolCreated = False
    
    _threadCount = 0
    _removeCount = 0

    @staticmethod
    def createPool(numThreads):
        '''
        Creates the initial pool of threads.
        If called more than once, it doesn't do anything subsequent times.
        '''
        if not UpdateThread._bPoolCreated:
            print("creating thread pool")
            UpdateThread._bPoolCreated = True
            UpdateThread.addThreads(numThreads)

    @staticmethod
    def addThreads(numThreads):
        '''
        Add threads to those currently running.
        '''
        print("adding threads:", numThreads)
        for x in range(numThreads):
            UpdateThread._threadCount += 1
            thread = UpdateThread()
            thread.daemon = True
            thread.start()

    @staticmethod
    def removeThreads(numThreads):
        '''
        Removes threads from those that are currently running.

        Works by having threads check to see if they should die off after they're done
        with a job. This way we don't interupt any work that is occuring.
        '''
        UpdateThread._removeCount += numThreads
        
    @staticmethod
    def addJob(observer):
        '''
        add a job to the jobPool
        '''
        UpdateThread.jobPool.put(observer)

    def run (self):
        '''
        will only return (die off) if _removeCount > 0
        '''
        while True:
            observer = UpdateThread.jobPool.get()

            # job processing
            if observer != None:
                observer.update()
            else:
                print("cannot process non-existent observer")
                
            # notify queue that job is done
            UpdateThread.jobPool.task_done()
            
            # whether thread should die off (in order to remove threads)
            lock = threading.Lock()
            with lock:
                #TODO: helper function?
                if UpdateThread._removeCount > 0:
                    UpdateThread._removeCount -= 1
                    print("Removing thread")
                    return
