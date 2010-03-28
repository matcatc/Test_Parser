'''
@date Feb, 28, 2010
@author: Matthew A. Todd
'''
import unittest
from BoostTestParser.TestResults.Notice import Notice
from BoostTestParser.Common.Constants import Constants

import io

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
        Constants.errStream = io.StringIO()
        self.notice = Notice(self.file, self.line, self.info, self.type)


    def tearDown(self):
        Constants.reset()
        del self.notice

    def test_fileDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.notice.file = "blah"
        del self.notice.file

    def test_lineDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.notice.line = 0
        del self.notice.line

    def test_infoDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.notice.info = "blah"
        del self.notice.info

    def test_typeDeleter(self):
        '''
        b/c the deleter isn't being run, we're going to just run it here.
        '''
        self.notice.type = "blah"
        del self.notice.type

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

    def test_emptyInfo(self):
        '''
        test that a warning is output when info is an empty string
        '''
        self.notice.info = ""
        self.assertEqual(Constants.errStream.getvalue(), Notice.EMPTY_INFO + "\n")

    def test_emptyType(self):
        '''
        test that a warning is output when type string is empty
        '''
        self.notice.type = ""
        self.assertEqual(Constants.errStream.getvalue(), Notice.EMPTY_TYPE + "\n")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
