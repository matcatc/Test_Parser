'''
@date Mar 6, 2010
@author: Matthew A. Todd
'''
from subprocess import Popen, PIPE
import sys, copy

class TestRunner(object):
    '''
    This object exists in order to run the external test
    program (BoostTest in the default case.) It contains
    information that allows it to spawn a subprocess
    (the test program.)
    
    @date Mar 6, 2010
    @author: Matthew A. Todd
    '''
    # BoostTest log_level options
    lvl_success = "success"
    lvl_test_suite = "test_suite"
    lvl_message = "message"
    lvl_warning = "warning"
    lvl_error = "error"

    def __init__(self):
        '''
        Constructor
        '''
        self.runner = None
        self.logLevel = TestRunner.lvl_test_suite
        
        
    def run(self, params):
        '''
        runs just with the given params. Concatenates runner and params.
        
        @return stdout from the test program
        '''
        try:
            # TODO: make sure cmd is correct
            # os.join()?
            cmd = copy.deepcopy(params)
            cmd.insert(0, self.runner)
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        except (OSError, ValueError):
            print("Failed to execute unit test program", file=sys.stderr)
            return None

        stdout, stderr = p.communicate()
        if not stderr == "":
            print(stderr.decode("utf-8"), file=sys.stderr)      
        return stdout
        

