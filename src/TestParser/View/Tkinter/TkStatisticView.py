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
from TestParser.Common.Constants import Constants

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
        Constants.logger.debug("removing statistic view")
        self.model.removeObserver(self)
        self.parent.destroy()
        
    def about(self, data=None):
        self.controller.displayAboutDialog(self.parent)
        
        
    def _setupUi(self):
        '''
        '''
        frame = tk.Frame(self.parent)
        frame.pack(expand=True, fill=tk.BOTH)
        
        # share area evenly between cols, main row has higher priority
        for col in range(3):
            frame.grid_columnconfigure(col, weight =1)
        frame.grid_rowconfigure(0, weight=2)
        frame.grid_rowconfigure(1, weight=1)
            

        self.parent.title("Test Parser Statistic - %s" % self.model.runnerName())
        
        
        # menu
        menubar = tk.Menu(self.parent)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=self.close, accelerator="Ctrl+Q")
        self.parent.bind("<Control-q>", self.close)
        self.parent.protocol('WM_DELETE_WINDOW', self.close)    # call our custom func when (x) button pressed
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about, accelerator="F1")
        self.parent.bind("<F1>", self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.parent.config(menu=menubar)


        # data display
        stickyAll = tk.N+tk.S+tk.W+tk.E
        
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
        Constants.logger.debug("updating Statistic view")
        self._display(self.controller.getResults())
        
    def _display(self, results):
        passes, fails, errors = ComputeStatistics.computeStatistics(results)
                
        self.passDisplay['text'] = str(passes)
        self.failDisplay['text'] = str(fails)
        self.errorDisplay['text'] = str(errors)