'''
@date Mar 6, 2010
@author: Matthew A. Tod
'''

class Observable(object):
    '''
    for observer pattern
    @date Mar 6, 2010
    @author: Matthew A. Todd
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.observers = set([])
        
    def registerObserver(self, observer):
        self.observers.add(observer)
    
    def removeObserver(self, observer):
        self.observers.discard(observer)
    
    def notifyObservers(self):
        for observer in self.observers:
            observer.update()
        