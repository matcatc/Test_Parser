'''
@date Mar 6, 2010
@author: Matthew A. Tod
'''

from  BoostTestParser.Common import UpdateThread

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
        '''
        uses threading
        '''
        for observer in self.observers:
            thread = UpdateThread.UpdateThread(observer)
            thread.start()
            
#    def notifyObservers(self):
#        '''
#        doesn't use threading
#        '''
#        for observer in self.observers:
#            observer.update()
        