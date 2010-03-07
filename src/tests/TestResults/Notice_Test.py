'''
@date Feb, 28, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.TestResults.Notice import Notice

class Notice_Test(unittest.TestCase):
    '''
    test: BoostTestParser.TestResults.Notice
    
    @date Feb, 28, 2010
    @author: Matthew A. Todd
    '''
    file = "main.cpp"
    line = 0
    info = "blah"
    type = "error"

    def setUp(self):
        self.notice = Notice(self.file, self.line, self.info, self.type)


    def tearDown(self):
        del self.notice
               
        
    def testValue(self):
        '''
        Test valid input: empty strings, negative numbers
        '''
        self.assertRaises(ValueError, Notice, "", self.line, self.info, self.type)
        self.assertRaises(ValueError, Notice, self.file, -1, self.info, self.type)

    def testGetters(self):
        '''
        test that getters return proper values.
        I know this is trivial, but I've already caught one mistake with it.
        '''
        self.assertEqual(self.notice.file, self.file)
        self.assertEqual(self.notice.line, self.line)
        self.assertEqual(self.notice.info, self.info)
        self.assertEqual(self.notice.type, self.type)

    def testToString(self):
        '''
        not much to test, so just make sure it returns a string
        '''
        self.assertTrue(isinstance(self.notice.toString(), str))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
