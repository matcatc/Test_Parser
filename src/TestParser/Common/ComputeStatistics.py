'''
@date Aug 16, 2010
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
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

def computeStatistics(result):
    '''
    @param result the results to compute statistics for
    @return tuple (passes, fails, errors)
    '''
    type = result.type.lower()
    if type == "pass" \
            or type == "ok":
        return (1, 0, 0)
    elif type == "fail":
        return (0, 1, 0)
    elif type == "error" \
            or type == "fatalerror":
        return (0, 0, 1)
#    else:
#        print("DEBUG: unknown type: %s" % result.type)
        
    passes = 0
    fails = 0
    errors = 0
    for child in result.getChildren():
        temp = computeStatistics(child)
        
        passes += temp[0]
        fails += temp[1]
        errors += temp[2]
        
    return (passes, fails, errors)
