''' 
@date Apr 17, 2010
@author: matcat
'''
import unittest

from BoostTestParser.Common.UpdateJobPool import UpdateThread

class UpdateThread_Test(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    
    def test_runNone(self):
        '''
        test that an error message is printed out when trying to process a
        job that is None
        '''
        raise NotImplementedError


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()