'''
@date Aug 13, 2010
@author: Matthew Todd
'''
import unittest
from TestParser.Common.ViewFactory import ViewFactory

class ViewFactory_Test(unittest.TestCase):
    '''
    Test ViewFactory
    
    Organized by ui framework (to ensure everything called at least once
    while minimizing duplicate calls.)
    
    @date Aug 13, 2010
    '''

    def test_textFramework(self):
        raise NotImplementedError()
    
    def test_qtFramework(self):
        '''
        TODO: can we really test?
        '''
        raise NotImplementedError()
    
    def test_tkinterFramework(self):
        raise NotImplementedError()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()