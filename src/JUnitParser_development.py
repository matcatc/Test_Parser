'''
This is a temporary file to help us exercise JUnitParser
'''

from TestParser.Parser.JUnitParser import JUnitParser

def main():
    parser4 = JUnitParser(4)
    
    f = open('/home/matcat/Desktop/Junit4_out')
    parser4.parse(file=f)


if __name__ == '__main__':
    main()