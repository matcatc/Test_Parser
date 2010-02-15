'''
Created on Feb 14, 2010

@author: matcat
'''

#
# There are several ways to proceed.
# - We can parse test cases and separate into passing and failing.
# - We can build some sort of GUI, which would allow us to user colors.
# - We can write into html, using colors as well
#    - no different than xslt, but with the ability to change into something else later
#
# matodd
#


from xml.etree import ElementTree as ET

def print_TestCase(testCase):
    nameIndent = "\t"
    indent = "\t\t"
    
    print nameIndent, testCase.get("name")
    print indent, "time:", testCase.find("TestingTime").text, "secs"
    
    
    error = testCase.find("Error")
    if error is not None:
        print indent, "file:", error.get("file")
        print indent, "line:", error.get("line")
        print indent, error.text
        
    return

def print_TestSuite(testSuite):
    indent = ""
    
    print indent, testSuite.get("name")
    for case in testSuite:
        print_TestCase(case)
        
    return

def print_TestLog(root):
    for suite in root:
        print_TestSuite(suite)
    
    return

def main():
    xml_file = "test.xml"
    
    try:
        tree = ET.parse(xml_file)
    except Exception, inst:
        print "Unexpected error opening %s: %s" % (xml_file, inst)
        return
    
    print_TestLog(tree.getroot())
    
    return
    

if __name__ == '__main__':
    main()
