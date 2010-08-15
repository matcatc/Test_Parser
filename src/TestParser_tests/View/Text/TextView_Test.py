'''
@date Apr 25, 2010
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

from TestParser.View.Text import TextView
from TestParser.Model import Model
from TestParser.Common.computeDataFilepath import computeDataFilepath


class TextView_Test(unittest.TestCase):
    '''
    I am not really sure what and how to test for this class.
    
    The only thing to really test with the display() methods is
    that there are no misspellings. But that would require feeding
    in data that would cause the methods to be completely executed.
    
    @see TestRunner_test for information regarding how Boost_Test may
    cause tests that use it to fail.
    '''

    def setUp(self):
        self.model = Model.Model()
        self.view = TextView.TextView(self.model)


    def tearDown(self):
        del self.model
        del self.view


    def test_registering(self):
        '''
        Test that the view registers itself with the model on creation
        '''
        self.assertTrue(self.view in self.model._observers)

    def test_update(self):
        '''
        checks that there are no exceptions raised. Won't actually do
        much of anything.
        '''
        self.view.update()
        
    def test_runView(self):
        '''
        Runs the view to make sure nothing explodes.
        '''
        model = Model.setupModel("Boost", computeDataFilepath("../../Model/sample/Boost_Test", __file__))
        
        from TestParser.Common.ViewFactory import ViewFactory
        ViewFactory.selectFramework("text")
        ViewFactory.preViewInit(model)
        ViewFactory.createResultView()
        ViewFactory.startApplication()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
