#!/usr/bin/python3
'''
For some modules (currently QtView and TextView,) we import where
used instead of the usual location. We do this because the modules
are only used once. And we don't need both, and the one we need
is decided at runtime. Similar to FrameworkFactoriy's import
situation.

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

from TestParser.Model import Model
from TestParser.Common.ViewFactory import ViewFactory
from TestParser.Common.TestFrameworkFactory import UndefinedTestFrameworkError
from optparse import OptionParser


def initConstants(options):
    '''
    initialize constants based on given program options
    
    @date Aug 9, 2010
    '''
    from TestParser.Common.Constants import CONSTANTS
    
    CONSTANTS.autoExpand = (False, True)[options.auto_expand == "on"]
    CONSTANTS.logger.info("autoExpand = %s" % options.auto_expand)

    CONSTANTS.threading = options.threading
    CONSTANTS.logger.info("threading = %s" % options.threading)
    

def main():
    '''    
    '''
    usage = "usage: %prog [options] <framework> <test_runner>"
    ui_choices = ("qt", "tkinter", "text")
    ui_help = "use specified ui framework. Default: text"
    ui_metavar = "/".join(ui_choices)
    view_choices = ("result", "statistic")
    view_help = "use specified views. Default: result"
    view_metavar = "/".join(view_choices)
    
    parser = OptionParser(usage)
    parser.add_option("--ui", dest="ui",
                      action="store", choices=ui_choices, metavar=ui_metavar,
                      default="text", help=ui_help)
    parser.add_option("--view", dest="views",
                      action="append", choices=view_choices,
                      metavar=view_metavar,
                      default=[], help=view_help)
    parser.add_option("--autoexpand", dest="auto_expand",
                      action="store", choices=("on", "off"),
                      default="on",help="enable/disable autoexpand",
                      metavar="on/off")
    parser.add_option("--threading", dest="threading",
                      action="store_true",
                      default=False, help="enable multi-threading")
    parser.add_option("-f", dest="fileRunner",
                      action="store_true", default=False,
                      help="use file instead of runner")
    
    (options, args) = parser.parse_args()   

    # should only have the test_runner
    if len(args) != 2:
        parser.error("Incorrect number of arguments")
    framework = args[0]
    runner = args[1]
    
    initConstants(options)
    
    try:
        model = Model.setupModel(framework, runner, options.fileRunner)
    except UndefinedTestFrameworkError as error:
        import sys
        print("Unknown test framework: %s" % error.framework)
        sys.exit()
    
    ## create views
    # default value.
    # if we do it through add_option, the default value will be there regardless
    # if we actually specify our own value (b/c its appending, not overwriting)
    if len(options.views) == 0:
        options.views = ["result"] 
    
    ViewFactory.selectFramework(options.ui, model)
    ViewFactory.createViews(options.views)
    ViewFactory.startApplication()

    
if __name__ == "__main__":
    main()
