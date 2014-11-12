import inspect, sys
from codex import chardict

# Debugging

def checkFail(r):

    superCaller = inspect.stack()[2][3]
    caller = inspect.stack()[1][3]
    if r is False:
        print("The following function failed: {}, called by {}".format(caller,superCaller))
        print("Got retVal of {}".format(r))
        exit()

def error(e):
    caller = inspect.stack()[1][3]
    tb = sys.exc_info()[2]
    print("Error caught in function {}:\n{}\n{}".format(caller,e,tb))


# General Functionality

def retInt(c):
    retVal = False

    try:
        c = str(c)
        retVal = int(chardict[c])

    except Exception as e:
        error(e)

    checkFail(retVal)
    return(retVal)

def retChar(n):
    retVal = False

    try:
        for key, value in chardict.items():
            if int(value) == n:
                retVal = key

    except Exception as e:
        error(e)

    checkFail(retVal)
    return(retVal)

def sumStr(s):
    retVal = False

    try:
        x = 0
        for i in s:
            y = retInt(i)
            x += y

        retVal = x

    except Exception as e:
        error(e)

    checkFail(retVal)
    return(retVal)

def meanStr(s):
    retVal = False

    try:
        s_len = len(s)
        s_sum = sumStr(s)
        s_mean = s_sum / s_len

        retVal = s_mean

    except Exception as e:
        error(e)

    checkFail(retVal)
    return(retVal)
