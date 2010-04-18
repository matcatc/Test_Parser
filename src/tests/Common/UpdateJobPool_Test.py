'''
@date Apr 17, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.Common.UpdateJobPool import UpdateJobPool


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
        result in an exception.
        '''
        raise NotImplementedError

    def test_removeThreads(self):
        '''
        tests that _removeCount is increased as appropriate and
        _threadCount decreases as appropriate.
        '''
        self.jobPool.createPool(UpdateJobPool_Test.cThreads)

        num = 2
        self.jobPool.removeThreads(num)
        self.assertEqual(self.jobPool._removeCount, num)

        
        for i in range(num):
            self.jobPool.addJob(None)
            
        self.jobPool.jobQueue.join()

        self.assertEqual(self.jobPool._removeCount, 0)
        self.assertEqual(self.jobPool._threadCount, UpdateJobPool_Test.cThreads - num)

    def test_addJob(self):
        raise NotImplementedError


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
