'''
@date Mar 21, 2010
@author Matthew A. Todd

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
from TestParser.Common.Observable import Observable
from .Mock_Observer import Mock_Observer


class Observable_Test(unittest.TestCase):
    '''
    Test Observable.
    
    @see TestParser.Common.Observable
    '''

    subscriber = Mock_Observer()
    subscriber2 = Mock_Observer()

    def setUp(self):
        self.subject = Observable()

    def tearDown(self):
        del self.subject

    def testRegister(self):
        self.subject.registerObserver(Observable_Test.subscriber)
        self.assertEqual(len(self.subject._observers), 1)
    
    def testRemove(self):
        self.subject.registerObserver(Observable_Test.subscriber)
        self.subject.registerObserver(Observable_Test.subscriber2)
        
        self.subject.removeObserver(Observable_Test.subscriber)
        self.assertEqual(len(self.subject._observers), 1)

        self.subject.removeObserver(Observable_Test.subscriber2)
        self.assertEqual(len(self.subject._observers), 0)        
        

    def testNotify_unthreaded(self):
        from TestParser.Common.Constants import Constants
        Constants.threading = False
        
        self.subject.registerObserver(Observable_Test.subscriber)
        self.subject.registerObserver(Observable_Test.subscriber2)
        
        self.subject.notifyObservers()
        
        self.assertTrue(Observable_Test.subscriber.notified)
        self.assertTrue(Observable_Test.subscriber2.notified)
        
    def testNotify_threaded(self):
        '''
        Test with threading.
        
        
        Need to create the job pool b/c threading is False by default,
        so the job pool isn't created during object initialization.
        Note that its fine during program execution, but needs to be
        done here. 
        '''
        from TestParser.Common.Constants import Constants
        Constants.threading = True
        self.subject._updateJobPool.createPool(2)
        
        self.subject.registerObserver(Observable_Test.subscriber)
        self.subject.registerObserver(Observable_Test.subscriber2)
        
        self.subject.notifyObservers()
        
        self.assertTrue(Observable_Test.subscriber.notified)
        self.assertTrue(Observable_Test.subscriber2.notified)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNotify']
    unittest.main()