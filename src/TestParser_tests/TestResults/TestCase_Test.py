'''
@date Feb 26, 2010
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
from TestParser.TestResults.TestCase import TestCase
from TestParser.TestResults.Notice import Notice

class TestCase_Test(unittest.TestCase):
    '''
    Test TestParser.TestResults.TestCase
    @date Feb 26, 2010
    @author Matthew A. Todd
    '''
    type = "error"
    file = "main.cpp"
    line = 0
    info = "blah"
    notice = Notice(file, line, info, type)

    def setUp(self):
        self.test = TestCase()


    def tearDown(self):
        self.test.types.clear()        # shouldn't have to have this line
        del self.test.notices[:]
        del self.test

    def test_timeTakenDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.test.timeTaken = 0
        del self.test.timeTaken

    def testHasType(self):
        '''
        check that type not present prior to adding
        check that it is present after
        '''
        self.assertFalse(self.test.hasType(self.type))
        
        self.test.addNotice(self.notice)
        self.assertTrue(self.test.hasType(self.type))
        
    def testName(self):
        '''
        test name setting and getting
        '''
        name = "testName"
        self.test.name = name
        self.assertEqual(self.test.name, name)
        
    def testTime(self):
        '''
        test time bogus input, setting and getting.
        
        We can't use assertRaises b/c its a property (as far as I know.)
        '''
        time = 123
        
        # bogus input
        try:
            self.test.timeTaken = -1
        except ValueError:
            passes = True
        finally:
            if not passes:
                self.fail("self.test.timeTaken = -1 did not throw an exception")

        # get/set equivalence
        self.test.timeTaken = time
        self.assertEqual(self.test.timeTaken, time)
    
    def testGetNotices(self):
        amount = 4
        
        for i in range(amount):
            self.test.addNotice(self.notice)
            
        self.assertTrue(self.notice in self.test.notices)
        self.assertEqual(len(self.test.notices), amount)

        
    def testGetNoticesOfType(self):
        '''
        check that getNoticesOfType returns the correct amount of the correct type
        '''
        amount = 5
        type = "testType"
        notice2 = Notice("file", 0, "newNotice", type)
        
        for i in range(3):
            self.test.addNotice(self.notice)
        for i in range(amount):
            self.test.addNotice(notice2)
        
        self.assertEquals(len(self.test.getNoticesOfType(type)), amount)
        self.assertTrue(notice2 in self.test.getNoticesOfType(type))
        
        
    def test_getChildren(self):
        '''
        test for typos and that function overridden
        '''
        self.test.getChildren()
        
    def test_getRelevantDisplayData(self):
        '''
        test that name and time data returned
        '''
        data = self.test.getRelevantDisplayData()
        types = [typeinfo for typeinfo, x in data]
        self.assertTrue("name" in types)
        self.assertTrue("time" in types)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
