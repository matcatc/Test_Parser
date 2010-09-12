'''
@date Sep 12, 2010
@author Matthew Todd
'''
import unittest
from TestParser.View.Text.TextViewController import TextViewController
from ..Controller_Test import Mock_Model

class TextViewController_Test(unittest.TestCase):

    def setUp(self):
        self.controller = TextViewController(Mock_Model())

    def test_reportException(self):
        self.controller.reportException(NotImplementedError)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()