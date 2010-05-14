#!/usr/bin/python3

from BoostTestParser.View import TextView
from BoostTestParser.View import QtView
import sys

from BoostTestParser.Model import Model
from BoostTestParser.Model import TestRunner
from BoostTestParser.Parser import BasicParser



def main():
    '''    
    TODO: allow user to choose Gui or Text output
    '''
    
    
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
