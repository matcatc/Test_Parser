'''
@date Aug 16, 2010
@author matcat
'''

def computeStatistics(result):
    type = result.type.lower()
    if type == "pass" \
            or type == "ok":
        return (1, 0, 0)
    elif type == "fail":
        return (0, 1, 0)
    elif type == "error" \
            or type == "fatalerror":
        return (0, 0, 1)
#    else:
#        print("DEBUG: unknown type: %s" % result.type)
        
    passes = 0
    fails = 0
    errors = 0
    for child in result.getChildren():
        temp = computeStatistics(child)
        
        passes += temp[0]
        fails += temp[1]
        errors += temp[2]
        
    return (passes, fails, errors)