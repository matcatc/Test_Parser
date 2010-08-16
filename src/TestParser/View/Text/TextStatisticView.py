'''
@date Aug 16, 2010
@author Matthew Todd
'''

from TestParser.Common import Observer, ComputeStatistics

class TextStatisticView(Observer.Observer):
    '''
    reports statistics/overall information about the test results
    
    @date Aug 16, 2010
    @author matcat
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.model.registerObserver(self)
        
        
    def _retrieveTestResults(self):
        '''
        get the test results from the model
        @return test results
        '''
        return self.model.results
    
    def update(self):
        '''
        For observer.
        
        display() automatically pulls results, so we can just rely on display()
        '''
        self.display()
        
    def display(self):
        '''
        pulls latest information and displays it.
        
        delegates to _display() for displaying
        '''
        results = self._retrieveTestResults()
        if results is None:
            print("No test results to display")
            return
        self._display(results)
        
    def _display(self, results):
        passes, fails, errors = ComputeStatistics.computeStatistics(results)
        
        print("%d pass, %d fail, %d error" % (passes, fails, errors))
        
            