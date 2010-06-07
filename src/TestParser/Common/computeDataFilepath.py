'''
@date Jun 7, 2010
@author Matthew A. Todd
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
