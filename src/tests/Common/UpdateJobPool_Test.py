'''
@date Apr 17, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.Common.UpdateJobPool import UpdateJobPool, NonExistentJobPool_Exception
from .Mock_Observer import Mock_Observer
import time

class UpdateJobPool_Test(unittest.TestCase):
    '''
    @date Apr 17 2010
    @author Matthew A. Todd
    '''
    cThreads = 3

    def setUp(self):
        self.jobPool = UpdateJobPool()

    def tearDown(self):
        del self.jobPool

    def test_jobPoolNotCreated(self):
        self.assertFalse(self.jobPool._bPoolCreated)

    def test_jobPoolCreation(self):
        self.jobPool.createPool(UpdateJobPool_Test.cThreads)
        self.assertEqual(self.jobPool._threadCount, UpdateJobPool_Test.cThreads)

    def test_addThreads(self):
        self.jobPool.createPool(UpdateJobPool_Test.cThreads)

        num = 2
        self.jobPool.addThreads(num)
        self.assertEqual(self.jobPool._threadCount, UpdateJobPool_Test.cThreads + num)

    def test_addThreadsToNonexistentJobPool(self):
        '''
        Trying to add threads to a pool that hasn't been created yet should
        result in an exception (NonExistentJobPool_Exception).
        '''
        self.assertRaises(NonExistentJobPool_Exception, self.jobPool.addThreads, 0)


    def test_removeThreads(self):
        '''
        tests that _removeCount is increased as appropriate and
        _threadCount decreases as appropriate.
        
        Due to thread timing, sometimes this won't pass b/c _removeCount
        decremented after waitUntilJobsFinished() returns, so I added a sleep()
        just to give it enough time to decrement. But still no guarantees.
        '''
        self.jobPool.createPool(UpdateJobPool_Test.cThreads)

        num = 2
        self.jobPool.removeThreads(num)
        self.assertEqual(self.jobPool._removeCount, num)
        
        for i in range(num):
            self.jobPool.addJob(None)
            
        self.jobPool.waitUntilJobsFinished_Raise()
        time.sleep(.2)

        self.assertEqual(self.jobPool._removeCount, 0)
        self.assertEqual(self.jobPool._threadCount, UpdateJobPool_Test.cThreads - num)

    def test_addJob(self):
        '''
        test that jobs are run. use mock object.
        '''
        self.jobPool.createPool(UpdateJobPool_Test.cThreads)
        
        observer = Mock_Observer()
        self.jobPool.addJob(observer)
        
        self.jobPool.waitUntilJobsFinished_Raise()
        
        self.assertTrue(observer.notified)
        
    def test_waitUntilJobsFinished_Raise(self):
        '''
        test that exception thrown when there are no threads
        '''
        self.assertRaises(NonExistentJobPool_Exception, self.jobPool.waitUntilJobsFinished_Raise)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
