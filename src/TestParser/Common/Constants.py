'''
@date Mar 28, 2010
@author Matthew A. Todd

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
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import logging


class Constants_class(object):
    '''
    contains project wide constants.
    
    Singleton pattern. Everyone should use static variable Constants, defined
    later in this module.
    
    errStream: error stream
     This way programs can use the error/warning that would be otherwise
     output strait to the console. Also very useful for testing purposes.
    
    logger: logging instance
     
    
    @date Mar 28, 2010
    @author Matthew A. Todd
    '''
    
    LOG_FILENAME = './TestParser.log'
    DEFAULT_ERR_STREAM = sys.stderr

    
    def __init__(self):
        '''
        Only values initialized in self.reset() should be changed after
        program initialization.
        '''
        # Set up a specific logger with our desired output level
        self.logger = logging.getLogger('TestParser_Logger')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(Constants_class.LOG_FILENAME, 'w')
        formatter = logging.Formatter("[%(levelname)s]\t %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        self.autoExpand = True
        
        self.threading = False
        
        self.errStream = self.DEFAULT_ERR_STREAM

    def resetErrStream(self):
        self.errStream = self.DEFAULT_ERR_STREAM
        
        
CONSTANTS = Constants_class()
