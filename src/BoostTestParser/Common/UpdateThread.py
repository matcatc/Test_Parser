'''
Created on Mar 14, 2010

@author: matcat
'''

import threading

class UpdateThread (threading.Thread):

    def __init__(self, target):
        '''
        target is the observer we're going to update
        '''
        threading.Thread.__init__(self)
        self.target = target

    def run (self):
        print("updating target: ", self.target)
        self.target.update()


