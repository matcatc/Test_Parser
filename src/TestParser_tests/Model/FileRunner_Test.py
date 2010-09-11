'''
Created on Sep 11, 2010

@author: matcat
'''
import unittest
from TestParser.Model.FileRunner import FileRunner, InvalidFileException
from TestParser.Common.computeDataFilepath import computeDataFilepath

class FileRunner_Test(unittest.TestCase):

    fileName = computeDataFilepath("./sample/FileRunner_test", __file__)
    fileData = "blah"

    def setUp(self):
        self.runner = FileRunner()


    def tearDown(self):
        del self.runner

    def test_runnerProperties(self):
        self.runner.runner = self.fileName
        self.assertEquals(self.runner.runner, self.fileName)
        del self.runner.runner

    def test_runFile(self):
        self.runner.runner = self.fileName
        output = self.runner.run()
        self.assertEquals(output, self.fileData)
        
    def test_runStdin(self):
        '''
        TODO: how to implement?
        '''
        raise NotImplementedError
        
        
    def test_runAll(self):
        self.runner.runner = self.fileName
        output = self.runner.runAll()
        self.assertEquals(output, self.fileData)
        
    def test_runPrevious(self):
        self.runner.runner = self.fileName
        output = self.runner.runPrevious()
        self.assertEquals(output, self.fileData)
        
    def test_runNonexistentFile(self):
        self.runner.runner = "fakeNonexistentFile_adkadf"
        self.assertRaises(InvalidFileException ,self.runner.run)
        
    ## exception tests
    
    def test_InvalidFileException(self):
        e = InvalidFileException("fakeNonexistentFile_aasdfalk")
        str(e)
        repr(e)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()