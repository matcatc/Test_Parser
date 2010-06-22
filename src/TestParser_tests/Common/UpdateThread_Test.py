''' 
@date Apr 17, 2010
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
import unittest

from TestParser.Common.UpdateJobPool import UpdateThread, UpdateJobPool
from TestParser.Common.Constants import Constants

import sys

import io

class UpdateThread_Test(unittest.TestCase):
    '''
    Since UpdateThread is something of a private/helper class, which
    isn't to be used by the outside world, we're going to test most
    of its functionality through UpdateThreadPool
    '''

    def setUp(self):
        '''
        Setup errStream last so that no garbage gets in during
        other initialization procedures.
        '''
        self.jobPool = UpdateJobPool()
        self.jobPool.createPool(1)
        
        Constants.errStream = io.StringIO()        


    def tearDown(self):
        Constants.reset()
        del self.jobPool
    
    
    def test_runNone(self):
        '''
        Test that an error message is printed out when trying to process a
        job that is None.
        
        Use MSG in stream so that if other stuff gets into the stream,
        we don't fail.
        '''
        self.jobPool.addJob(None)
        self.jobPool.waitUntilJobsFinished_Raise()
        # TODO: can we check the log instead?
        # that way we can ditch the printing to errStream
        self.assertTrue(UpdateThread.NON_EXISTENT_OBSERVER_MSG + "\n" in Constants.errStream.getvalue())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()