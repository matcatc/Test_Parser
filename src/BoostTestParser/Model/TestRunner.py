'''
@date Mar 6, 2010
@author: Matthew A. Todd
'''
from subprocess import Popen, PIPE
import sys, copy, os.path

class TestRunner(object):
    '''
    This object exists in order to run the external test
    program (BoostTest in the default case). It contains
    information that allows it to spawn a subprocess
    (the test program.)
    
    @date Mar 6, 2010
    @author Matthew A. Todd
    '''
    # BoostTest log_level options
    lvl_success = "success"
    lvl_test_suite = "test_suite"
    lvl_message = "message"
    lvl_warning = "warning"
    lvl_error = "error"
    
    # BoostTest format
    format = "--log_format=XML"

    def __init__(self):
        '''
        Constructor
        '''
        ## name / path of the test program to be run 
        self.runner = None
        self.logLevel = TestRunner.lvl_test_suite
    
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
    
    
    def run(self, params):
        '''
        runs just with the given params. Concatenates runner and params.
        
        TODO: check that self.runner is not None?
        
        @param params list of params to be passed to the test runner.
            The same params you would use if running on the command line.
        @return stdout from the test program. Or None if program execution failed.
        '''
        try:
            cmd = copy.deepcopy(params)
            cmd.insert(0, self.runner)                
            cmd.insert(1, TestRunner.format)
            cmd.insert(2, "--log_level="+self.logLevel)
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        except (OSError, ValueError):
            print("Failed to execute unit test program", file=sys.stderr)
            return None

        stdout, stderr = p.communicate()
        if not stderr == "":
            print(stderr.decode("utf-8"), file=sys.stderr)      
        return stdout
    
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
