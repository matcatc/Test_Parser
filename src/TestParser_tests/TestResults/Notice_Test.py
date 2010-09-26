'''
@date Feb, 28, 2010
@author: Matthew A. Todd

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
from TestParser.TestResults.Notice import Notice
from TestParser.Common.Constants import CONSTANTS

import io

class Notice_Test(unittest.TestCase):
    '''
    test: TestParser.TestResults.Notice
    
    @date Feb, 28, 2010
    @author: Matthew A. Todd
    '''
    file = "main.cpp"
    line = 0
    info = "blah"
    type = "error"

    def setUp(self):
        CONSTANTS.errStream = io.StringIO()
        self.notice = Notice(self.file, self.line, self.info, self.type)


    def tearDown(self):
        CONSTANTS.resetErrStream()
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
        Test invalid input: negative line numbers
        '''
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
        Test that nothing explodes
        '''
        self.notice.info = ""

    def test_emptyType(self):
        '''
        Test that nothing explodes
        '''
        self.notice.type = ""
        
    def test_emptyFIle(self):
        '''
        Test that nothing explodes
        '''
        self.notice.file = ""
        
    def test_noneLine(self):
        '''
        Test that nothing explodes
        '''
        self.notice.line = None

    def test_getChildren(self):
        length = len(self.notice.getChildren())
        self.assertEqual(length, 0)
        
    def test_getRelevantDisplayData(self):
        '''
        test that file, line, and info data is returned
        '''
        data = self.notice.getRelevantDisplayData()
        types = [infotype for infotype, x in data]              #@UnusedVariable
        self.assertTrue("file" in types)
        self.assertTrue("line" in types)
        self.assertTrue("info" in types)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
