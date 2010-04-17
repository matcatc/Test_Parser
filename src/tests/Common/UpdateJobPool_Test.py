'''
@date Apr 17, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.Common.UpdateJobPool import UpdateJobPool


class UpdateJobPool_Test(unittest.TestCase):
    def setUp(self):
        self.jobPool = UpdateJobPool()

    def tearDown(self):
        pass

    def test_jobPoolNotCreated(self):
        self.assertFalse(self.jobPool._bPoolCreated)

    def test_jobPoolCreation(self):
        cThreads = 3
        self.jobPool.createPool(cThreads)
        
        self.assertEqual(self.jobPool._threadCount, cThreads)
        
    def test_addThreads(self):
        raise NotImplementedError
    
    def test_addThreadsToNonexistentJobPool(self):
        raise NotImplementedError
    
    def test_removeThreads(self):
        raise NotImplementedError
    
    def test_addJob(self):
        raise NotImplementedError


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()