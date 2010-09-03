'''
@date Aug 13, 2010
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
from TestParser.Common.ViewFactory import ViewFactory, UndefinedView, UndefinedViewFramework
from TestParser.Model import Model
from TestParser.Common.computeDataFilepath import computeDataFilepath

class ViewFactory_Test(unittest.TestCase):
    '''
    Test ViewFactory
    
    Organized by ui framework (to ensure everything called at least once
    while minimizing duplicate calls.)
    
    @date Aug 13, 2010
    '''
    def setUp(self):
        self.model = Model.setupModel("Boost",
                     computeDataFilepath("../Model/sample/Boost_Test", __file__))

    def test_UndefinedUi(self):
        self.assertRaises(UndefinedViewFramework, ViewFactory.selectFramework,
                           "nonexistent_framework_that_won't_be_created")
        
    def test_UndefinedView(self):
        self.assertRaises(UndefinedView, ViewFactory.createViews, ["undefined_view"])

    def test_textFramework(self):
        ViewFactory.selectFramework("text")
        ViewFactory.preViewInit(self.model)
        ViewFactory.createViews(["result", "statistic"])
        ViewFactory.startApplication()

    
    def test_qtFramework(self):
        '''
        Test the parts that we can. Currently unable to test startApplicaton()
        b/c it would start an event loop which we'd be unable to stop. 
        '''
        ViewFactory.selectFramework("qt")
        ViewFactory.preViewInit(self.model)
        ViewFactory.createResultView()
        ViewFactory.createStatisticView()
        
        # this is where startApplication() would go
        # but can we really test? We need a way to close/shut it down
    
    def test_tkinterFramework(self):
        ViewFactory.selectFramework("tkinter")
        ViewFactory.preViewInit(self.model)
        ViewFactory.createResultView()
        ViewFactory.createStatisticView()
        
        # this is where startApplication() would go
        # but can we really test? We need a way to close/shut it down
    
    
    ## Test exceptions
    def test_UndefinedViewFramework_Exception(self):
        '''
        Test that nothing explodes
        '''
        exception = UndefinedViewFramework("unknown_gui_framework")
        repr(exception)
        
    def test_UndefinedView_Exception(self):
        '''
        Test that nothing explodes
        '''
        exception = UndefinedView("uknown_view")
        repr(exception)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()