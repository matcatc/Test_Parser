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

from TestParser.View import TextView
from TestParser.Model import Model, TestRunner
from TestParser.Parser import BasicParser



class TextView_Test(unittest.TestCase):
    '''
    I am not really sure what and how to test for this class.
    
    The only thing to really test with the display() methods is
    that there are no misspellings. But that would require feeding
    in data that would cause the methods to be completely executed.
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
        self.assertTrue(self.view in self.model.observers)

    def test_update(self):
        '''
        checks that there are no exceptions raised. Won't actually do
        much of anything.
        '''
        self.view.update()

    def test_startView(self):
        '''
        checks that no exceptions raised.
        
        Run twice just to see any problems occur (not actually looking
        for though.)
        
        Will fail if "tests/Model/Boost_Test" doesn't point to a real
        test runner.
        '''
        model = Model.Model()
        runner = TestRunner.TestRunner()
        runner.runner = "tests/Model/Boost_Test"
        model.testRunner = runner
        model.parser = BasicParser.BasicParser()

        TextView.TextView.startView(model)
        TextView.TextView.startView(model)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
