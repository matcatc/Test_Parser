'''
@date Mar 12, 2010
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

import sys
from TestParser.Common.Constants import Constants

try:
    from PyQt4 import uic #@UnresolvedImport
    from PyQt4 import QtGui #@UnresolvedImport
except:
    sys.exit("Failed to import PyQt4. QtView needs PyQt4 in order to function. Please install PyQt4 or choose another UI.")

from TestParser.Common.computeDataFilepath import computeDataFilepath

from . import Controller
from . import About

filename = "MainWindow.ui"

UiClass, WidgetClass = uic.loadUiType(computeDataFilepath(filename, __file__))

class QtView(UiClass, WidgetClass):
    '''
    Main window for our Qt implemented view.
    
    colorBrushes is a dictionary mapping from item type (e.g: error, suite)
    to the color brush to use when displaying the item type. 
    
    DEFAULT_BRUSH is the brush/color to use when colorBrushes doesn't
    contain the key.
    
    PROPAGATING_ITEMS is a list of all items whose colors should propagate up.
    I.e: if one of these items is present, the higher level items will be
    colored according to the particular item's color. Items earlier in the
    list have a higher priority.
    
    MAX_PRIORITY is an number representing the highest priority
    of items in PROPAGATING_ITEMS. Its used in _priorityItem() as a return
    when the item isn't present.
    
    TODO: I think colors and propagating should be put someplace else.
    That
    way they can be used by other GUIs. Note that we'd have to use Abstract
    Factory or something similar for Brushes, so that we could use different
    GUI frameworks (The issue is that the brushes are Qt Objects.) Or 
    perhaps we should use strategy pattern or pass in our desired values.
    We're going to want to wait until we need to share or until we need
    to refactor.
    '''

    _red = QtGui.QColor("red")
    _green = QtGui.QColor("green")
    _white = QtGui.QColor("white")

    _redBrush = QtGui.QBrush(_red)
    _greenBrush = QtGui.QBrush(_green)
    _whiteBrush = QtGui.QBrush(_white)

    DEFAULT_BRUSH = _whiteBrush


    colorBrushes = {'error' : _redBrush,
                    'fatalerror' : _redBrush,
                    'fail' : _redBrush,
                    'pass' : _greenBrush,
                    'ok' : _greenBrush,
                    'message' : _whiteBrush,
                    'suite' : _greenBrush,
                    'testresults' : _greenBrush,
                    'testcase' : _greenBrush}

    PROPAGATING_ITEMS = ['error', 'fatalerror', 'fail']
    MAX_PRIORITY = len(PROPAGATING_ITEMS) + 1

    TYPE_COL = 0
    NAME_COL = 1
    FILE_COL = 2
    LINE_COL = 3
    INFO_COL = 4
    TIME_COL = 4


    def __init__(self, model, controller):
        '''
        Constructor
        '''
        WidgetClass.__init__(self)
        self.setupUi(self)

        self.model = model
        self.model.registerObserver(self)

        # To be set by controller
        self.controller = controller


#
# User interfacing code
#

    def aboutDialog(self):
        '''
        Menu Cmd. Display about dialog.
        
        Modal.
        @date Jun 17, 2010
        '''
        self.controller.displayAboutDialog()

    def reRun(self):
        '''
        Rerun previous test configuration.
        
        Will expand items in the tree according to the following:
        If there are items selected at rerun, then those items are
        expanded/displayed. If none selected, then the items 
        expanded/displayed at rerun will be so after.
        
        @date Jun 17, 2010
        '''
        Constants.logger.debug("start of QtView.reRun()")
        
        if Constants.autoExpand:
            itemsToExpand = []
            selectedItems = self.treeWidget.selectedItems()
            if len(selectedItems) > 0:
                for item in selectedItems:
                    itemsToExpand.append(self._computeItemPath(item))
            else:          
                itemsToExpand = self._getExpandedItems()

        self.controller.runPrevious()

        if Constants.autoExpand:
            Constants.logger.debug("itemsToExpand:\t %s" % itemsToExpand)
            self._expandItems(itemsToExpand)
        
        Constants.logger.debug("end of QtView.reRun()")

#
## auto expand
#

    def _computeItemPath(self, item):
        '''
        Compute and return the path from root to given item.
        
        Path is a list. The first item is the root and each element
        is a child of its predecessor item.
        
        Builds path from head to tail.
        
        @date Jul 30, 2010
        '''
        path = []
        while item is not None:
            path.insert(0, self._getItemData(item))
            item = item.parent()
        return path

    def _getExpandedItems(self):
        '''
        Returns a list of items that are open/displayed/expanded.
        
        Only add items who don't have expanded children b/c those
        who do will be expanded during their children's expansion.
        
        @date Jul 29, 2010
        '''
        itemsToExpand = []
        iter = QtGui.QTreeWidgetItemIterator(self.treeWidget)
        while iter.value():
            item = iter.value()
            if item.parent() is not None:
                if item.parent().isExpanded() and not item.isExpanded():
                    itemsToExpand.append(self._computeItemPath(item))
            iter += 1
            
        return itemsToExpand

    def _expandItems(self, itemsToExpand):
        '''
        Expands items in the tree so that the user can see them.
        
        @warning This currently only works if there is only a single
        root item. But Test Results is setup such that it always returns
        a single root item, so it shouldn't be a problem. Nevertheless,
        we should at some point make this more resilient.
        
        TODO: what if we have multiple root/top-level items?
        I think because of the way we setup _expandPath(), we
        can just run this on all roots/topLevelItems. We'll need to test
        somehow, but I don't think we'll ever encounter a situation with
        multiple roots. So we'll leave it be for the moment.
        
        @param itemsToExpand a list of item paths to expand along.
        
        @date Jul 29, 2010
        '''
        for path in itemsToExpand:
            root = self.treeWidget.topLevelItem(0)          
            self._expandPath(path, root)

    def _expandPath(self, path, root):
        '''
        Expands a path.
        
        Because there will be multiple children that satisfy the
        requirements at any particular level (think multiple unnamed suites),
        we need and thus use a backtracking algorithm.
        
        We expand items on the way back up (if returns true)
        
        @bug doesn't expand root
        
        @param path List of items. Path goes from parent to child
        @param root item in tree. Path starts at this item/root.
        @return True if parent item should be expanded.
        
        @date Jul 20, 2010
        '''       
        if len(path) == 0:
            return True
        
        if path[0] == self._getItemData(root):
            # no children and last item in path
            if root.childCount() == 0 and len(path) == 1:
                self.treeWidget.expandItem(root.parent())
                return True
            
            for i in range(root.childCount()):      # for child in root
                child =  root.child(i)
                
                if self._expandPath(path[1:], child):
                    self.treeWidget.expandItem(root.parent())
                    return True
                
        return False

    
    def _getItemData(self, item):
        '''
        Returns a tuple (type, name, file, line time) of
        the data contained within item.
        
        @date Jul 29, 2010
        '''
        if item is None:
            return None
        else:
            return (item.text(QtView.TYPE_COL),
                    item.text(QtView.NAME_COL),
                    item.text(QtView.FILE_COL),
                    item.text(QtView.LINE_COL),
                    item.text(QtView.INFO_COL))

#
# Data display code
#


    def _retrieveTestResults(self):
        '''
        get the test results from the model
        @return test results
        '''
        return self.model.results

    def update(self):
        '''
        For observer.
        '''
        self._updateTreeWidget(self._retrieveTestResults())

    def _clearTreeWidget(self):
        '''
        Clear out the TreeWidget.
        
        We have this function b/c treeWidget.clear() has some nasty side
        effects (seg-fault.) So we simply remove all the items and
        delete them by hand. We let the gc do all the clean up work.
        
        @date Jun 18, 2010
        '''
        while(self.treeWidget.takeTopLevelItem(0) is not None):
            pass


    def _updateTreeWidget(self, results):
        '''
        Actually update the GUI treeView widget
        '''

        self._clearTreeWidget()
        tree = self.treeWidget

        self.numCols = self.treeWidget.columnCount()
        self._displayResults(tree, results)


    def _displayResults(self, parent, result):
        '''
        @param parent is the parent item in the tree
        @param results results is all the Test Results data we want to 
            display below given parent item
            
        @return returns (item, brush) if a particular brush/color should
            propagate up (eg: we had an error, therefore error's color
            should work its way up)
        
        @date Jun 23, 2010
        '''
        resultItem = QtGui.QTreeWidgetItem(parent)

        self._displayData(resultItem, result)

        returnedBrushItems = []        # returned (item, brush) tuple
        for child in result.getChildren():
            temp = self._displayResults(resultItem, child)

            if temp is not None:
                returnedBrushItems.append(temp)

        return self._colorRow(resultItem, result, returnedBrushItems)

    def _displayData(self, resultItem, result):
        '''
        Parses relevant display data and displays it.
        
        helper function for _displayResults()
        
        @see _displayResults()
        
        @param resultItem QtItem that we're coloring
        @param result TestComposite data to display
        
        @date Jun 26, 2010
        '''
        resultItem.setText(QtView.TYPE_COL, result.type)

        for infotype, data in result.getRelevantDisplayData():
            if infotype == "name":
                resultItem.setText(QtView.NAME_COL, data)
            elif infotype == "file":
                resultItem.setText(QtView.FILE_COL, data)
            elif infotype == "line":
                resultItem.setText(QtView.LINE_COL, data)
            elif infotype == "info":
                resultItem.setText(QtView.INFO_COL, data)
            elif infotype == "time":
                if data is not None:
                    resultItem.setText(QtView.TIME_COL, "time: " + data)

    def _colorRow(self, resultItem, result, returnedBrushItems):
        '''
        Determine which brush/color to use and color the row.
        
        helper function for _displayResults()
        
        Returns (item, brush) if the brush is to propagate up.
        @see _displayResults()
        
        @param resultItem QtItem that we're coloring
        @param result TestComposite data to display
        @param returnedBrushItems list of (item, brush) tuples that were
            returned by child items. Contains brushes that are trying
            to propagate up.
        
        @return item, brush tuple if brush should propagate up.
        @date Jun 26, 2010
        '''
        # get highest priority brush of those propagating up
        propagateItem = None
        propagateBrush = None
        for item, brush in returnedBrushItems:
            if item is not None and brush is not None:
                if QtView._priorityItem(item) \
                        < QtView._priorityItem(propagateItem):
                    propagateItem = item
                    propagateBrush = brush


        # get brush for current item
        try:
            brush = QtView.colorBrushes[result.type.lower()]
        except KeyError:
            brush = QtView.DEFAULT_BRUSH


        thisPropagateUp = result.type.lower() in QtView.PROPAGATING_ITEMS
        childPropagateUp = propagateBrush is not None

        # determine which brush to use
        if thisPropagateUp and childPropagateUp:
            if QtView._priorityItem(propagateItem) \
                    < QtView._priorityItem(result.type):
                self._colorRow_helper(resultItem, propagateBrush)
                return (propagateItem, propagateBrush)
            else:
                self._colorRow_helper(resultItem, brush)
                return (result.type, brush)
        elif thisPropagateUp:
            self._colorRow_helper(resultItem, brush)
            return (result.type, brush)
        elif childPropagateUp:
            self._colorRow_helper(resultItem, propagateBrush)
            return (propagateItem, propagateBrush)
        else:
            self._colorRow_helper(resultItem, brush)
            return None

    def _colorRow_helper(self, item, brush):
        '''
        Colors a given item across all cols (the entire row)
        with the given brush.
        
        helper function for _colorRow()
        
        TODO: better name?
        
        @date Jun 23, 2010
        '''
        for i in range(self.numCols):
            item.setBackground(i, brush)

    @staticmethod
    def _priorityItem(item):
        '''
        Determines the priority of an item in PROPAGATING_ITEMS. Lower
        values have more priority.
        
        Returning MAX_PRIORITY so that we don't have to deal with None
        where this function is returned.
        
        helper function
        
        @return priority of item or MAX_PRIORITY if not in list
        @date Jun 26, 2010
        '''
        try:
            return QtView.PROPAGATING_ITEMS.index(item.lower())
        except:         # TODO specific exception
            return QtView.MAX_PRIORITY


class QtViewController(Controller.Controller):
    '''
    A simple controller for QtView.
    
    Nothing to override
    @see Controller.Controller
    '''

    def displayAboutDialog(self):
        '''
        Displays the Qt based About Dialog
        '''
        widget = About.About()
        widget.exec()
