'''
Created on Apr 25, 2010

@author: matcat
'''
import unittest

from BoostTestParser.View.Controller import Controller

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
        
    def test_update(self):
        '''
        test update doesn't throw any exceptions.
        
        Doesn't test functionality
        '''
        self.controller.update()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()