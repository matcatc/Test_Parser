'''
@date Apr 25, 2010
@author: Matthew A. Todd
'''
import unittest

from BoostTestParser.View import TextView
from BoostTestParser.Model import Model, TestRunner
from BoostTestParser.Parser import BasicParser



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
