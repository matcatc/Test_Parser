'''
@date Mar 6, 2010
@author: Matthew A. Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>
'''
from TestParser.Common.Constants import Constants
from subprocess import Popen, PIPE
import copy, os.path

class TestRunner(object):
    '''
    This object exists in order to run the external test
    program (BoostTest in the default case). It contains
    information that allows it to spawn a subprocess
    (the test program.)
    
    @note this is currently setup for Boost's Test framework. If we
    want to add other frameworks later, we're probably going to have to
    use some sort of pattern.
    
    @date Mar 6, 2010
    @author Matthew A. Todd
    '''
    # BoostTest log_level options
    LOG_LVL_SUCCESS = "success"
    LOG_LVL_TESTSUITE = "test_suite"
    LOG_LVL_MESSAGE = "message"
    LOG_LVL_WARNING = "warning"
    LOG_LVL_ERROR = "error"
    
    ## BoostTest format
    LOG_FORMAT = "--log_format=XML"

    ## message that is displayed when testRunner isn't run successfully
    EXECUTION_FAILURE_MESSAGE = "Failed to execute unit test program"
    
    ## message for when no previous cmd to rerun
    NO_PREVIOUS_CMD_MESSAGE = "No previous cmd to rerun. Running all."

    def __init__(self):
        '''
        Constructor
        '''
        ## string containing name / path of the test program to be run 
        self.runner = None
        self.logLevel = TestRunner.LOG_LVL_TESTSUITE
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
            return None
        
        try:
            if givenCmd:
                cmd = givenCmd
            else:
                cmd = copy.deepcopy(params)
                cmd.insert(0, self.runner)                
                cmd.insert(1, TestRunner.LOG_FORMAT)
                cmd.insert(2, "--log_level="+self.logLevel)
                self.previousCmd = cmd
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        except (OSError, ValueError):
            print(TestRunner.EXECUTION_FAILURE_MESSAGE, file=Constants.errStream)
            return None

        stdout, stderr = p.communicate()
        if not stderr == "":
            print(stderr.decode("utf-8"), file=Constants.errStream)      
        return stdout
    
    def runPrevious(self):
        '''
        runs using the same settings/configuration as the previous run.
        
        @date Jun 16, 2010
        '''
        if self.previousCmd is None:
            # error/raise etc
            Constants.logger.warning(TestRunner.NO_PREVIOUS_CMD_MESSAGE)
            return self.runAll()
        return self.run(givenCmd = self.previousCmd)
            
        
            
    
    def runAll(self):
        '''
        runs all tests in the test program
        @return return from run()
        '''
        return self.run([])
    
    def runTest(self, tests):
        '''
        @param tests A list (something iterable) of names of tests to be run
        @return return from run() 
        --run_test=testA,testB
        '''
        param = "--run_test=" + ",".join(tests)
        return self.run([param])

    def runSuite(self, suites):
        '''
        according to: http://www.boost.org/doc/libs/1_42_0/libs/test/doc/html/utf/user-guide/runtime-config/run-by-name.html
        running suites and tests is the same
        
        @param suites A list (something iterable) of names of suites to be run
        @return return from runTest()
        '''
        return self.runTest(suites)
