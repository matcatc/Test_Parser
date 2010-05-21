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
from BoostTestParser.Common.Observable import Observable
from .Mock_Observer import Mock_Observer


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