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
from optparse import OptionParser


def initConstants(options):
    '''
    initialize constants based on given program options
    
    @date Aug 9, 2010
    '''
    from TestParser.Common.Constants import Constants
    
    Constants.autoExpand = (False, True)[options.auto_expand == "on"]
    Constants.logger.info("autoExpand = %s" % options.auto_expand)

    Constants.threading = options.threading
    Constants.logger.info("threading = %s" % options.threading)
    

def main():
    '''    
    '''
    usage = "usage: %prog [options] <test_runner>"
    ui_choices = ("qt", "tkinter", "text")
    ui_help = "use specified ui framework: " + ", ".join(ui_choices) + ".\nDefault: text"
    view_choices = ("result", "statistic")
    view_help = "use specified views: " + ", ".join(view_choices) + ".\nDefault: result"
    framework_choices = ("Boost", "PyUnittest", "JUnit")
    framework_help = "use specified test framework: %s"   \
                            % ", ".join(framework_choices)
    
    parser = OptionParser(usage)
    parser.add_option("--ui", dest="ui",
                      action="store", choices=ui_choices,
                      default="text", help=ui_help)
    parser.add_option("--view", dest="views",
                      action="append", choices=view_choices,
                      default=[], help=view_help)
    parser.add_option("--framework", dest="framework",
                      action="store", choices=framework_choices,
                      help=framework_help)
    parser.add_option("--autoexpand", dest="auto_expand",
                      action="store", choices=("on", "off"),
                      default="on",help="enable/disable autoexpand")
    parser.add_option("--threading", dest="threading",
                      action="store_true",
                      default=False, help="enable multi-threading")
    
    (options, args) = parser.parse_args()   

    # should only have the test_runner
    if len(args) != 1:
        parser.error("Incorrect number of arguments")
    
    initConstants(options)
    
    model = Model.setupModel(options.framework, args[0])
    
    ## create views
    # default value.
    # if we do it through add_option, the default value will be there regardless
    # if we actually specify our own value (b/c its appending, not overwriting)
    if len(options.views) == 0:
        options.views = ["result"] 
    
    ViewFactory.selectFramework(options.ui)
    ViewFactory.preViewInit(model)
    ViewFactory.createViews(options.views)
    ViewFactory.startApplication()

    
if __name__ == "__main__":
    main()
