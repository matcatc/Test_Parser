'''
@date Mar 28, 2010
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
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

import tkinter as tk
from tkinter import ttk

from TestParser.Common import Observer

class TkResultView(Observer.Observer):
    '''
    classdocs
    @date Aug 28, 2010
    @author matcat
    '''


    def __init__(self, parent, model, controller):
        '''
        Constructor
        
        @param parent the tkinter parent item for this view
        '''
        self.parent = parent
        
        self.model = model
        self.model.registerObserver(self)

        self.controller = controller
        
        self._setupUi()
        
    def _setupUi(self):
        frame = tk.Frame(self.parent)
        frame.pack()

        self.parent.title("Test Parser - %s" % ' '.join(self.model.testRunner.runner))

        # sample code
        self.button = tk.IntVar()
        
        tk.Radiobutton(frame, text="Radio Button 1", variable=self.button, \
                value=1).pack(anchor=tk.W)
        tk.Radiobutton(frame, text="Radio Button 2", variable=self.button, \
                value=2).pack(anchor=tk.W)
        tk.Radiobutton(frame, text="Radio Button 3", variable=self.button, \
                value=3).pack(anchor=tk.W)


        tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X,  \
                                                         padx=5, pady=5)

        tk.Button(frame, text="Update").pack()