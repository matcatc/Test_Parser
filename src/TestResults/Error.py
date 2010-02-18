'''
Created on Feb 17, 2010

@author: matcat
'''

class Error:
    '''
    classdocs
    '''

    file = ""
    line = 0
    prob = ""

    def __init__(self, file, line, prob):
        '''
        file and prob are of type String
        line is an int
        '''
        self.file = file
        self.line = line
        self.prob = prob
        
        
    def toString(self):
        return "in %s at line %d: %s" % (self.file, self.line, self.prob)