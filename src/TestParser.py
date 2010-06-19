#!/usr/bin/python3
'''
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

from TestParser.View import TextView
from TestParser.View import QtView
from TestParser.Model import Model
from TestParser.Model import TestRunner
from TestParser.Parser import BoostParser

from optparse import OptionParser


def main():
    '''    
    '''
    
    usage = "usage: %prog [options] <test_runner>"
    gui_choices = ("Simple (Default)",)
    gui_help = "use specified gui: " + ", ".join(gui_choices)
    
    parser = OptionParser(usage)
    parser.add_option("--text", dest="ui", const="text",
                      action="store_const",
                      help="use text/console output")
    parser.add_option("--gui", dest="gui",
                      action="store", choices=gui_choices,
                      help=gui_help)
    
    (options, args) = parser.parse_args()    

    # should only have the test_runner
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    
    # setup model
    model = Model.Model()
    runner = TestRunner.TestRunner()
    runner.runner = args[0]
    model.testRunner = runner
    model.parser = BoostParser.BoostParser()
    
    if options.ui == "text":
        TextView.TextView.startView(model)
    else:
        QtView.QtView.startView(model)

    
if __name__ == "__main__":
    main()
