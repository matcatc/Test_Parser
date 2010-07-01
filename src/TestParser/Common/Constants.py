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

    
    def __init__(self):
        '''
        '''
        self.handler = logging.FileHandler(Constants_class.LOG_FILENAME, 'w')
        self.reset()
    
    def reset(self):
        '''
        reset all the values to their default values
        '''
        self.errStream = sys.stderr
        
        # Set up a specific logger with our desired output level
        self.logger = logging.getLogger('TestParser_Logger')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)

        
        
Constants = Constants_class()