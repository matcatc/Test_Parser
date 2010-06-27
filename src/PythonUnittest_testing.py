'''
For testing PythonUnittest parser
'''

from TestParser.Parser.PythonUnittestParser import PythonUnittestParser
from TestParser.View.TextView import TextView
from TestParser.Model import Model

def main():
    parser = PythonUnittestParser()
    f = open('/home/matcat/Desktop/python_unittest')
    
    results = parser.parse(file=f)
    
    model = Model.Model()
    view = TextView(model)
    view._display(results)
    
if __name__ == '__main__':
    main()