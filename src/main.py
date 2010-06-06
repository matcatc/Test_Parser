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
import sys

from TestParser.Model import Model
from TestParser.Model import TestRunner
from TestParser.Parser import BasicParser



def main():
    '''    
    TODO: allow user to choose Gui or Text output
    '''
    
    print("DEBUG: argv:" ,file=sys.stderr)
    for x in sys.argv:
        print("\t", x, file=sys.stderr)
    if len(sys.argv) < 2:
        print("Usage: test parser <test_runner>")
        return
    
    # setup model
    model = Model.Model()
    runner = TestRunner.TestRunner()
    runner.runner = sys.argv[1]
    model.testRunner = runner
    model.parser = BasicParser.BasicParser()
    
    if len(sys.argv) > 2 and sys.argv[2] == "--text":
        TextView.TextView.startView(model)
    else:
        QtView.QtView.startView(model)

    
if __name__ == "__main__":
    main()
