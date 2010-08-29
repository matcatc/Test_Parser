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
    @date Aug 28, 2010
    @author matcat
    '''
    
    tagColors = {'error' : 'red',
                    'fatalerror' : 'red',
                    'fail' : 'red',
                    'pass' : 'green',
                    'ok' : 'green',
                    'message' : 'white',
                    'suite' : 'green',
                    'testresults' : 'green',
                    'testcase' : 'green'} 


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
        
    def rerun(self, data=None):
        #TODO: add auto-expand
        self.controller.runPrevious()
        
    def about(self, data=None):
        self.controller.displayAboutDialog()
        
    def _setupUi(self):
        '''
        
        Note that treeviews have an extra column for some reason, which is why we
        just specify one less.
        '''
        frame = tk.Frame(self.parent)
        frame.pack()

        self.parent.title("Test Parser - %s" % ' '.join(self.model.testRunner.runner)) #TODO: refactor
        
        
        # menu
        menubar = tk.Menu(self.parent)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=self.close, accelerator="Ctrl+Q")
        self.parent.bind("<Control-q>", self.close)
        menubar.add_cascade(label="File", menu=filemenu)
        
        runmenu = tk.Menu(menubar, tearoff=0)
        runmenu.add_command(label="Rerun", command=self.rerun, accelerator="Ctrl+R")
        self.parent.bind("<Control-r>", self.rerun)
        menubar.add_cascade(label="Run", menu=runmenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about, accelerator="F1")
        self.parent.bind("F1", self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.parent.config(menu=menubar)


        # tree
        treeCols = ('Name', 'File', 'Line', 'Info')
        self.tree = ttk.Treeview(frame, columns=treeCols)
        
        for col in treeCols:
            self.tree.heading(col, text=col)
            
        self.tree.tag_configure('green', background='green')
        self.tree.tag_configure('red', background='red')
        
        self.tree.pack()
        self.rootId = None
        
    #
    ## result displaying
    #
    
    def update(self):
        '''
        For observer.
        '''
        self._updateTreeWidget(self.controller.getResults())
    
    def _clearTreeWidget(self):
        if self.rootId is not None:
            print("deleting rootId %s" % self.rootId)
            self.tree.delete(self.rootId)
    
    def _updateTreeWidget(self, results):
        self._clearTreeWidget()
        
        self._displayResults('', results)
        
    
    def _displayResults(self, parentId, result):
        '''
        @param parent is the parent item in the tree
        @param results results is all the Test Results data we want to 
            display below given parent item
            
        @return returns (item, brush) if a particular brush/color should
            propagate up (eg: we had an error, therefore error's color
            should work its way up)
        
        @date Jun 23, 2010
        '''
        tag = TkResultView.tagColors[result.type.lower()]
        id = self.tree.insert(parentId, 'end', text=result.type,
                               values=self._getDisplayData(result),
                               tags=(tag))
        
        # if this is a root item, save its id
        if parentId == '':
            self.rootId = id


        returnedTags = [tag]        # returned (item, brush) tuple
        for child in result.getChildren():
            temp = self._displayResults(id, child)

            if temp is not None:
                returnedTags.append(temp)

        tag = self._getHighestPriorityTag(result, returnedTags)
        
        self.tree.item(id, tags=(tag))

        return tag
    
    def _getHighestPriorityTag(self, result, returnedTags):
        if 'red' in returnedTags:
            return 'red'
        elif 'green' in returnedTags:
            return 'green'
        else:
            return 'white'
    
    def _getDisplayData(self, result):
        '''
        Parses relevant display data and displays it.
        
        helper function for _displayResults()
        
        @see _displayResults()
        
        @param resultItem QtItem that we're coloring
        @param result TestComposite data to display
        
        @date Jun 26, 2010
        '''

        name = file = line = info = ""

        for infotype, data in result.getRelevantDisplayData():
            if infotype == "name":
                name = data
            elif infotype == "file":
                file = data
            elif infotype == "line":
                line = data
            elif infotype == "info":
                info = data
            elif infotype == "time":
                if data is not None:
                    info = data
                    
        return (name, file, line, info)
