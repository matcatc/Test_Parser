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

from TestParser.View.Controller import Controller

class Mock_Model(object):
    '''
    Mock model for testing purposes.
    
    Only has one observer at a time (for simplicity's sake.)
    '''
    def registerObserver(self, observer):
        self.observer = observer
        
    def runAll(self):
        '''
        no need to implement, just checking correctly spelled.
        '''
        pass
    
    def runPrevious(self):
        '''
        no need to implement, just checking correctly spelled.
        '''
        pass
        

class ControllerTest(unittest.TestCase):


    def setUp(self):
        self.model = Mock_Model()
        self.controller = Controller(self.model)

    def tearDown(self):
        del self.model


    def test_initRegistering(self):
        '''
        test that controller is registered with model
        
        create our own local version just to make sure its being
        initialized the way we want.
        '''
        controller = Controller(self.model)
        self.assertTrue(controller == self.model.observer)
        
    def test_run(self):
        '''
        test run doesn't throw any exceptions.
        
        Doesn't test functionality
        '''
        self.controller.run()
        
    def test_runPrevious(self):
        '''
        tests that nothing explodes
        
        @date Jul 29, 2010
        '''
        self.controller.runPrevious()
        
    def test_update(self):
        '''
        test update doesn't throw any exceptions.
        
        Doesn't test functionality
        '''
        self.controller.update()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()