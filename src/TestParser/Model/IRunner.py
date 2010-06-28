'''
@date Jun 28, 2010
@author matcat
'''

import os.path

class IRunner(object):
    '''
    classdocs
    @date Jun 28, 2010
    @author matcat
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ## string containing name / path of the test program to be run 
        self.runner = None
        self.previousCmd = None
    
    @property
    def runner(self):
        return self._runner
    @runner.setter
    def runner(self, runner): #@DuplicatedSignature
        '''
        This automatically deals with path names.
        If None: None
        If valid for cwd: use cwd
        else: global path
        
        @pre runner is present in working directory or global path
        @param runner filename/path to the test runner
        '''
        if runner is None:
            self._runner = None
        # working directory   
        elif os.path.exists(os.path.abspath(runner)):            
            self._runner = os.path.abspath(runner)
        # global path
        else:
            self._runner = runner
    @runner.deleter
    def runner(self): #@DuplicatedSignature
        del self._runner
        
    def run(self, params = None, givenCmd = None):
        '''
        generic run command
        
        To be implemented in subclass
        
        @param params list of params to be passed to the test runner.
            The same params you would use if running on the command line.
        @param givenCmd a string explicitly stating the cmd to be executed.
            Used by runPrevious(). Could also be called by client or others
            if they wanted to execute a specific cmd.
        @return stdout from the test program. Or None if program execution failed.
        '''
        raise NotImplementedError
    
    def runPrevious(self):
        '''
        runs using the same settings/configuration as the previous run
        
        To be implemented in subclass
        '''
        raise NotImplementedError
    
    def runAll(self):
        '''
        runs all tests in the test program
        
        To be implemented in subclass
        '''
        raise NotImplementedError
        
        