'''
Created on Mar 14, 2010

@author: matcat
'''
import threading, queue
#import sys     # for debug statement

class UpdateThread ( threading.Thread ):
    '''
    Job is to update a given target. So jobPool contains observers
    '''
    # Note that these are static variables
    jobPool = queue.Queue(0)

    bPoolCreated = False

    _threadCount = 0    # might want to use a property to keep clients from changing this value.


    _removeCount = 0    # might want to use a property to keep clients from changing this value
    lock = threading.Lock() # for use when removing threads (in run())

    @staticmethod
    def createPool(numThreads):
        '''
        Creates the initial pool of threads.
        If called more than once, it doesn't do anything subsequent times.
        '''
        if not UpdateThread.bPoolCreated:
            print("creating thread pool")
            UpdateThread.bPoolCreated = True
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
        UpdateThread.jobPool.put(observer)
        

    def run ( self ):
        '''
        will only return if _removeCount > 0
        '''
        while True:
            observer = UpdateThread.jobPool.get()

            # job processing
            if observer != None:
                #print("DEBUG: updating target:" , observer, file=sys.stderr)
                observer.update()
            else:
                print("cannot process non-existent observer")
                
            # notify queue that job is done
            UpdateThread.jobPool.task_done()

            # whether thread should die off (in order to remove threads)
            with UpdateThread.lock:
                if UpdateThread._removeCount > 0:
                    UpdateThread._removeCount -= 1
                    print("Removing thread")
                    return
