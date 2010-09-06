'''
@date Aug 17, 2010
@author: Matthew Todd

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
from TestParser.View.Text import TextStatisticView
from TestParser.View.Text import TextViewController
from TestParser.Model import Model
from TestParser.Common.computeDataFilepath import computeDataFilepath

class MockModel(Model.Model):
    def __init__(self, results):
        super().__init__()
        self.results = results
            
class TextStatisticView_Test(unittest.TestCase):
    
    def setUp(self):
        self.model = Model.Model()
        self.controller = TextViewController.TextViewController(self.model)
        self.view = TextStatisticView.TextStatisticView(self.model, self.controller)
        
    def teardown(self):
        del self.model
        del self.controller
        del self.view
    
    def test_displayNone(self):
        '''
        Test display code when model doesn't contain any data
        '''
        model = MockModel(None)
        TextStatisticView.TextStatisticView(model, self.controller)
        
        model.notifyObservers()
        
    def test_update(self):
        '''
        Test that nothing explodes
        '''
        self.view.update()
        
    def test_runView(self):
        '''
        Runs the view to make sure nothing explodes.
        '''
        model = Model.setupModel("Boost", computeDataFilepath("../../Model/sample/Boost_Test", __file__))
        
        from TestParser.Common.ViewFactory import ViewFactory
        ViewFactory.selectFramework("text", model)
        ViewFactory.createResultView()
        ViewFactory.startApplication()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()