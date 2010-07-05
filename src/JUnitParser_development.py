'''
This is a temporary file to help us exercise JUnitParser
'''

from TestParser.Parser.JUnitParser import JUnitParser

def main():
    parser4 = JUnitParser(3)
    
    f = open('/home/matcat/Desktop/test_out')
    parser4.parse(file=f)
    
    print("Done.")


if __name__ == '__main__':
    main()