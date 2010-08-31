'''
@date Aug 28, 2010
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

import tkinter as tk
from tkinter import ttk

from TestParser.Common import Observer, ComputeStatistics

class TKStatisticView(Observer.Observer):
    '''
    @date Aug 30, 2010
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
        
    #
    ## callbacks and initialization
    #
    
    def close(self, data=None):
        self.model.removeObserver(self)
        self.parent.destroy()
        
    def about(self, data=None):
        self.controller.displayAboutDialog()
        
        
    def _setupUi(self):
        '''
        '''
        frame = tk.Frame(self.parent)
        frame.pack(expand=True, fill=tk.BOTH)

        self.parent.title("Test Parser Statistic - %s" % ' '.join(self.model.testRunner.runner)) #TODO: refactor
        
        
        # menu
        menubar = tk.Menu(self.parent)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=self.close, accelerator="Ctrl+Q")
        self.parent.bind("<Control-q>", self.close)
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about, accelerator="F1")
        self.parent.bind("F1", self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.parent.config(menu=menubar)


        # data display
        tk.Label(frame, text="Pass", fg="green", width=5).grid(row=0, column=0)
        tk.Label(frame, text="Fail", fg="red", width=5).grid(row=0, column=1)
        tk.Label(frame, text="Error", fg="red", width=5).grid(row=0, column=2)
        
        self.passDisplay = tk.Label(frame, text="0", fg="green")
        self.passDisplay.grid(row=1, column=0)
        self.failDisplay = tk.Label(frame, text="0", fg="red")
        self.failDisplay.grid(row=1, column=1)
        self.errorDisplay = tk.Label(frame, text="0", fg="red")
        self.errorDisplay.grid(row=1, column=2)

        
    #
    ## result displaying
    #
    
    def update(self):
        '''
        For observer.
        '''
        self._display(self.controller.getResults())
        
    def _display(self, results):
        passes, fails, errors = ComputeStatistics.computeStatistics(results)
                
        self.passDisplay['text'] = str(passes)
        self.failDisplay['text'] = str(fails)
        self.errorDisplay['text'] = str(errors)