from BoostTestParser.View import TextView
from BoostTestParser.View import QtView
import sys

def main():
    '''
    TODO: deal with duplication
    There is a lot of repetition between QtView and TextView's main.
    I.e: make this function do all the work.
    
    TODO: allow user to choose Gui or Text output
    '''
    if len(sys.argv) > 2 and sys.argv[2] == "--text":
        TextView.main()
    else:
        QtView.main()
    

if __name__ == "__main__":
    main()
