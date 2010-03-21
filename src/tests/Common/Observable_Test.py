'''
Created on Mar 21, 2010

@author: matcat
'''
import unittest
from BoostTestParser.Common.Observable import Observable
from BoostTestParser.Common.Observer import Observer

class Mock_Observer(Observer):
    
    def __init__(self):
        self.notified = False
    
    def update(self):
        self.notified = True

class Observable_Test(unittest.TestCase):
    '''
    Test Observable.
    
    @see BoostTestParser.Common.Observable
    '''

    subscriber = Mock_Observer()
    subscriber2 = Mock_Observer()

    def setUp(self):
        self.subject = Observable()

    def tearDown(self):
        del self.subject

    def testRegister(self):
        self.subject.registerObserver(Observable_Test.subscriber)
        self.assertEqual(len(self.subject.observers), 1)
    
    def testRemove(self):
        self.subject.registerObserver(Observable_Test.subscriber)
        self.subject.registerObserver(Observable_Test.subscriber2)
        
        self.subject.removeObserver(Observable_Test.subscriber)
        self.assertEqual(len(self.subject.observers), 1)

        self.subject.removeObserver(Observable_Test.subscriber2)
        self.assertEqual(len(self.subject.observers), 0)        
        

    def testNotify(self):
        self.subject.registerObserver(Observable_Test.subscriber)
        self.subject.registerObserver(Observable_Test.subscriber2)
        
        self.subject.notifyObservers()
        
        self.assertTrue(Observable_Test.subscriber.notified)
        self.assertTrue(Observable_Test.subscriber2.notified)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNotify']
    unittest.main()