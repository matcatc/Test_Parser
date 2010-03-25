'''
@date Feb 26, 2010
@author Matthew A. Todd
'''
import unittest
from BoostTestParser.TestResults.TestCase import TestCase
from BoostTestParser.TestResults.Notice import Notice

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
        test time bogus input, setting and getting
        '''
        time = 123
        
        # TODO: better way
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
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
