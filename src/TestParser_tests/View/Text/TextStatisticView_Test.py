'''
@date Aug 17, 2010
@author: Matthew Todd
'''
import unittest
from TestParser.Common.Observable import Observable
from TestParser.View.Text.TextStatisticView import TextStatisticView

class Model(Observable):
    def __init__(self, results):
        super().__init__()
        self.results = results
            
class TextStatisticView_Test(unittest.TestCase):
    def test_displayNone(self):
        '''
        Test display code when model doesn't contain any data
        '''
        model = Model(None)
        TextStatisticView(model)
        
        model.notifyObservers()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()