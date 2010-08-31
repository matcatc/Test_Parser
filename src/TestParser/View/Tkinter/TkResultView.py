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
from TestParser.Common.Constants import Constants

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
        '''
        auto-expand.
        
        It appears there is no way to deselect items in a treeview.
        Also, expanding an item selects it. So if the user has expanded
        any items, there will be a selection. So either something has
        been selected or nothing has been expanded. Therefore we don't
        have to check for expanded items when nothing is selected.
        '''
        Constants.logger.debug("start of QtResultView.reRun()")
        
        if Constants.autoExpand:
            itemsToExpand = []
            selectedItems = self.tree.selection()
            print("DEBUG: selectedItems = %s" % str(selectedItems))
            if len(selectedItems) > 0:
                for item in selectedItems:
                    itemsToExpand.append(self._computeItemPath(item))

        self.controller.runPrevious()

        if Constants.autoExpand:
            Constants.logger.debug("itemsToExpand:\t %s" % itemsToExpand)
            self._expandItems(itemsToExpand)
        
        Constants.logger.debug("end of QtResultView.reRun()")
        
        
    def about(self, data=None):
        self.controller.displayAboutDialog(self.parent)
        
    def _setupUi(self):
        '''
        
        Note that treeviews have an extra column for some reason, which is why we
        just specify one less.
        '''
        frame = tk.Frame(self.parent)
        frame.pack(expand=True, fill=tk.BOTH)

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
        self.parent.bind("<F1>", self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.parent.config(menu=menubar)


        # tree
        treeCols = ('Name', 'File', 'Line', 'Info')
        self.tree = ttk.Treeview(frame, columns=treeCols)
        
        for col in treeCols:
            self.tree.heading(col, text=col)
            
        self.tree.tag_configure('green', background='green')
        self.tree.tag_configure('red', background='red')
        
        self.tree.pack(expand=True, fill=tk.BOTH)
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
        @param parent is the parent item id in the tree
        @param results results is all the Test Results data we want to 
            display below given parent item
            
        @return returns tag/color that should
            propagate up (eg: we had an error, therefore error's color
            should work its way up)
        
        @date Aug 29, 2010
        '''
        id = self.tree.insert(parentId, 'end', text=result.type,
                               values=self._getDisplayData(result))
        
        # if this is a root item, save its id
        if parentId == '':
            self.rootId = id

        currItemColor = TkResultView.tagColors[result.type.lower()]
        returnedColors = [currItemColor]
        for child in result.getChildren():
            temp = self._displayResults(id, child)

            if temp is not None:
                returnedColors.append(temp)

        color = self._getHighestPriorityColor(returnedColors)        
        self.tree.item(id, tags=(color))
        return color
    
    def _getHighestPriorityColor(self, returnedColors):
        '''
        Determines which tag/color should propagate up.
        '''
        if 'red' in returnedColors:
            return 'red'
        elif 'green' in returnedColors:
            return 'green'
        else:
            return 'white'
    
    def _getDisplayData(self, result):
        '''
        Takes a TestComposite and returns its data in a tuple that can
        be used by the tkinter functions.

        @param result TestComposite data to display
        @date Aug 29, 2010
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

#
## auto expand
#

    def _computeItemPath(self, itemId):
        '''
        Compute and return the path from root to given item.
        
        Path is a list. The first item is the root and each element
        is a child of its predecessor item.
        
        Builds path from head to tail.
        
        @date Jul 30, 2010
        '''
        path = []
        while itemId != '':
            path.insert(0, self._getItemData(itemId))
            itemId = self.tree.parent(itemId)
        return path
    
    def _getItemData(self, itemId):
        '''
        Returns a tuple (type, name, file, line time) of
        the data contained within item.
        
        @date Aug 30, 2010
        '''
        itemData = self.tree.item(itemId)

        return (itemData['text'],) + tuple(itemData['values'])
                
    def _expandItems(self, itemsToExpand):
        '''
        Expand all items so user can see them

        
        @param itemsToExpand a list of item paths to expand along.
        
        @date Aug 30, 2010
        '''
        for path in itemsToExpand:
            print("DEBUG: path = %s" % path)
            self._expandPath(path, self.rootId)
            
    def _expandPath(self, path, currId, parentId=None):
        '''
        Expands a path.
        
        Because there will be multiple children that satisfy the
        requirements at any particular level (think multiple unnamed suites),
        we need and thus use a backtracking algorithm.
                        
        Because of tkinter's see(), we can just call on the final item in the list.
        So we go down to final item, then call see().
        
        @param path List of items. Path goes from parent to child
        @param currId Id of current item in tree. Path starts at this item.
        @param parentId Id of the parent item to this current item. Used so that
            we don't expand one too far and don't have to call extra see()'s
            (while recursing back up.)
        @return True if we've expanded the final item (no more backtracking, just
            go back up stack frames.
        
        @date Aug 30, 2010
        '''
        if len(path) == 0:
            if parentId != None:
                self.tree.see(parentId)
            return True
        
        if path[0] == self._getItemData(currId):
            children = self.tree.get_children(currId)
            
            # no children and last item in path
            if len(children) == 0 and len(path) == 1:
                self.tree.see(currId)
                return True
            
            for childId in children:
                if self._expandPath(path[1:], childId, currId):
                    return True
                
        return False

