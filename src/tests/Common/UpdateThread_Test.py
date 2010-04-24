''' 
@date Apr 17, 2010
@author: matcat
'''
import unittest

from BoostTestParser.Common.UpdateJobPool import UpdateThread, UpdateJobPool
from BoostTestParser.Common.Constants import Constants

import io

class UpdateThread_Test(unittest.TestCase):
    '''
    Since UpdateThread is something of a private/helper class, which
    isn't to be used by the outside world, we're going to test most
    of its functionality through UpdateThreadPool
    '''

    def setUp(self):
        Constants.errStream = io.StringIO()
        self.jobPool = UpdateJobPool()
        self.jobPool.createPool(1)

    def tearDown(self):
        Constants.reset()
        del self.jobPool
    
    
    def test_runNone(self):
        '''
        test that an error message is printed out when trying to process a
        job that is None
        '''
        self.jobPool.addJob(None)
        self.jobPool.waitUntilJobsFinished_Raise()
        self.assertEqual(Constants.errStream.getvalue(), UpdateThread.NON_EXISTENT_OBSERVER_MSG + "\n")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()