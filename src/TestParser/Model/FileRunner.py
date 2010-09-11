'''
@date Sep 10, 2010
@author Matthew Todd

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

#from .IRunner import IRunner
from TestParser.Common.Constants import Constants
import sys

class FileRunner():
    '''
    Not an actual runner in the normal sense. Reads in a data file (possibly
    stdin) and passes the data on.
    
    We use @property runner for two reasons:
        1) so that the interface matches (our file is set/get/del with the
             name runner)
        2) so that we can set runnerName
        
    @date Sep 10, 2010
    '''
    def __init__(self):
        self._file = None
        self.runnerName = None
        
    @property
    def runner(self):
        return self._file
    @runner.setter
    def runner(self, gRunner): #@DuplicatedSignature
        '''
        @param runner filename/path to the file
        '''
        self.runnerName = gRunner
        self._file = gRunner
        
    @runner.deleter
    def runner(self): #@DuplicatedSignature
        del self._file
        
    def run(self):
        try:
            if self._file == "-":
                return sys.stdin.read()
            with open(self._file, 'r') as f:
                return f.read()
        except:
            Constants.logger.error("Failed to read file %s" % self._file)
            return None
        
    def runAll(self):
        return self.run()
        
    def runPrevious(self):
        '''
        Log b/c runPrevious with Files can lead to unexpected behavior.
        '''
        Constants.logger.info("Running previous FileRunner, file = %s" % self._file)
        return self.run()