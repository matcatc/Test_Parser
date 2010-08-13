'''
@date Aug 13, 2010
@author: Matthew Todd
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
        ViewFactory.createViews(["result"])
        
        # static view not implemented yet
        self.assertRaises(NotImplementedError, ViewFactory.createViews, ["statistic"])
        
        ViewFactory.startApplication()

    
    def test_qtFramework(self):
        '''
        TODO: can we really test?
        '''
        raise NotImplementedError()
    
    def test_tkinterFramework(self):
        raise NotImplementedError()
    
    
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