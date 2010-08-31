'''
@date Aug 31, 2010
@author Matthew Todd
'''

import tkinter as tk
from tkinter import ttk

class TkAbout(object):
    '''
    About dialog box
    '''
    
    aboutText = "Test Parser is a developer tool that I built to help me and other developers visualize test results.\n" \
            "\n"\
            "I designed it to be extensible, so that it could display the results of multiple Test Frameworks. So if there is a framewok you would like to be able to parse, feel free to email me or implement yourself.\n" \
            "\n"\
            "License:    GNU GPL v3\n"\
            "Hosted:     http://github.com/matcatc/Test_Parser\n"\
            "Website:     http://matodd.x10hosting.com/programs/TestParser.html\n"\
            "\n"\
            "Matthew A. Todd\n"\
            "matcatprg@yahoo.com"
    
    def close(self, data=None):
        self.window.destroy()
    
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)        
        
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill=tk.BOTH)
        
        # display message
        text = tk.Label(frame, text=self.aboutText, justify=tk.LEFT,
                                wraplength=700)
        text.pack(expand=True, fill=tk.BOTH)
        
        # closing
        closeButton = tk.Button(frame, text="Close", command=self.close)
        closeButton.pack()
        self.window.bind("<Control-q>", self.close)