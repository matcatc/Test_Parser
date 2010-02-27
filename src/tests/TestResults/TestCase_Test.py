'''
@date Feb 26, 2010
@author Matthew A. Todd
'''
import unittest
from BoostTestParser.TestResults.TestCase import TestCase
from BoostTestParser.TestResults.Notice import Notice

from BoostTestParser.Exception.NoneError import NoneError


class TestCase_Test(unittest.TestCase):
    '''
    Test BoostTestParser.TestResults.TestCase
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
        self.test._types.clear()        # shouldn't have to have this line
        #del self.test._notices[:]
        self.test = None


    def testHasType(self):
        '''
        check that type not present prior to adding
        check that it is present after
        '''
        self.assertFalse(self.test.hasType(self.type))
        
        self.test.add(self.notice, self.type)
        self.assertTrue(self.test.hasType(self.type))
        
    def testName(self):
        '''
        test name setting and getting
        '''
        name = "testName"
        self.test.setName(name)
        self.assertEqual(self.test.getName(), name)
        
    def testTime(self):
        '''
        test time bogus input, setting and getting
        '''
        time = 123
        
        # bogus input
        self.assertRaises(NoneError, self.test.setTimeTaken, None)    
        self.assertRaises(ValueError, self.test.setTimeTaken, -1)
        
        # get/set equivalence
        self.test.setTimeTaken(time)
        self.assertEqual(self.test.getTimeTaken(), time)
    
    def testAdd(self):
        # bogus input
        self.assertRaises(NoneError, self.test.add, None, self.type)
        self.assertRaises(NoneError, self.test.add, self.notice, None)
        
    def testGetNotices(self):
        self.test.add(self.notice, self.type)
        self.assertTrue(self.notice in self.test.getNotices())
        
    def testGetNoticesOfType(self):
        '''
        check that getNoticesOfType returns the correct amount of the correct type
        '''
        amount = 5
        type = "testType"
        notice2 = Notice("file", 0, "newNotice", type)
        
        for i in range(3):
            self.test.add(self.notice, self.type)
        for i in range(amount):
            self.test.add(notice2, type)
        
        self.assertEquals(len(self.test.getNoticesOfType(type)), amount)
        self.assertTrue(notice2 in self.test.getNoticesOfType(type))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
