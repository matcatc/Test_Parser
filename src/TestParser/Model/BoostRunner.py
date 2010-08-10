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

from .IRunner import IRunner

class BoostRunner(IRunner):
    '''
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

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.logLevel = BoostRunner.LOG_LVL_TESTSUITE
    
    def computeCmd(self, params):
        '''
        Of the format:
            <runner> --log_format=XML --log_level=<level>
        
        @date Jun 28, 2010
        '''
        return self.runner + [BoostRunner.LOG_FORMAT,
                              "--log_level="+self.logLevel] \
                            + params
    
    def runTest(self, tests):
        '''
        @param tests A list (something iterable) of names of tests to be run
        @return return from run() 
        --run_test=testA,testB
        '''
        param = "--run_test=%s" % ",".join(tests)
        return self.run([param])

    def runSuite(self, suites):
        '''
        according to: http://www.boost.org/doc/libs/1_42_0/libs/test/doc/html/utf/user-guide/runtime-config/run-by-name.html
        running suites and tests is the same
        
        @param suites A list (something iterable) of names of suites to be run
        @return return from runTest()
        '''
        return self.runTest(suites)
