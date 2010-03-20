from BoostTestParser.View import TextView
from BoostTestParser.View import QtView
import sys

# TODO: allow user to choose Gui or Text output
if __name__ == "__main__":
    '''
    TODO: deal with duplication
    There is a lot of repetition between QtView and TextView's main.
    '''
    if len(sys.argv) > 2 and sys.argv[2] == "--text":
        TextView.main()
    else:
        QtView.main()
    
