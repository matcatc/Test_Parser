'''
@date Jun 7, 2010
@author Matthew A. Todd

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

import os.path

def computeDataFilepath(filename, calling_file):
    """
    compute the abs path of a file (filename) in same directory as calling_file
    
    @param filename the filename of the interesting file relative to the calling_file
    @param the file that is calling (pass in __file__)
    @warning we can't use __file__ if with py2exe
    @see http://stackoverflow.com/questions/2985755/accessing-files-after-setup-py-install
    """
    file_path = os.path.dirname(calling_file)
    return os.path.abspath(os.path.join(file_path, filename))
