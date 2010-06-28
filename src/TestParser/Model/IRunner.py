'''
@date Jun 28, 2010
@author matcat
'''
from TestParser.Common.Constants import Constants
import os.path
from subprocess import Popen, PIPE

class IRunner(object):
    '''
    classdocs
    @date Jun 28, 2010
    @author matcat
    '''

    ## message that is displayed when testRunner isn't run successfully
    EXECUTION_FAILURE_MESSAGE = "Failed to execute unit test program"
    
    ## message for when no previous cmd to rerun
    NO_PREVIOUS_CMD_MESSAGE = "No previous cmd to rerun. Running all."
    
    ## message for when runner is None
    RUNNER_NONE = "warning: runner is none"

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
        runs just with the given params. Concatenates runner and params.
        
        @param params list of params to be passed to the test runner.
            The same params you would use if running on the command line.
        @param givenCmd a string explicitly stating the cmd to be executed.
            Used by runPrevious(). Could also be called by client or others
            if they wanted to execute a specific cmd.
        @return stdout from the test program. Or None if program execution failed.
        '''
        if self.runner is None:
            # TODO: raise an exception?
            Constants.logger.warning(IRunner.RUNNER_NONE)
            return None
        
        try:
            if givenCmd:
                cmd = givenCmd
            else:
                cmd = self.computeCmd(params)
                self.previousCmd = cmd
                
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        except (OSError, ValueError):
            Constants.logger.error(IRunner.EXECUTION_FAILURE_MESSAGE)
            return None

        stdout, stderr = p.communicate()
        if not stderr == "":
            print(stderr.decode("utf-8"), file=Constants.errStream)      
        return stdout
    
    def computeCmd(self, params):
        '''
        Computes the cmd to be invoked in order to run the runner
        for the particular subclass.
        
        Think Template Method.
        
        To be overridden.
        
        @date Jun 28, 2010
        '''
        raise NotImplementedError
    
    def runPrevious(self):
        '''
        runs using the same settings/configuration as the previous run.
        
        @date Jun 16, 2010
        '''
        if self.previousCmd is None:
            # error/raise etc
            Constants.logger.warning(IRunner.NO_PREVIOUS_CMD_MESSAGE)
            return self.runAll()
        return self.run(givenCmd = self.previousCmd)
    
    def runAll(self):
        '''
        runs all tests in the test program
        @return return from run()
        '''
        return self.run([])
        
        