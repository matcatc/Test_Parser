'''
Created on Mar 27, 2010

@author: matcat
'''
import unittest
from BoostTestParser.Common import Observer

class Observer_Test(unittest.TestCase):


    def setUp(self):
        self.observer = Observer.Observer()


    def tearDown(self):
        del self.observer


    def test_notify(self):
        self.assertRaises(NotImplementedError, self.observer.notify)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()