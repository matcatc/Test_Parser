'''
@date Aug 16, 2010
@author Matthew Todd
'''

from TestParser.Common import Observer

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
        
        stats = self._computeStatistics(results)
        
        print("%d pass, %d fail, %d error" % (stats[0], stats[1], stats[2]))
        
    def _computeStatistics(self, result):
        type = result.type.lower()
        if type == "pass" \
                or type == "ok":
            return (1, 0, 0)
        elif type == "fail":
            return (0, 1, 0)
        elif type == "error" \
                or type == "fatalerror":
            return (0, 0, 1)
        else:
            print("ERROR: unknown type: %s" % result.type)
            
        passes = 0
        fails = 0
        errors = 0
        for child in result.getChildren():
            temp = self._computeStatistics(child)
            
            passes += temp[0]
            fails += temp[1]
            errors += temp[2]
            
        return (passes, fails, errors)
            