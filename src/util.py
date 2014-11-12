import inspect
from codex import chardict

# Debugging

def checkFail(r):
    caller = inspect.stack()[2][3]
    if r == False:
        print("The following function failed: {}".format(caller))
        sys.exit()

def error(e):
    caller = inspect.stack()[2][3
    print("Error caught in function {}:\n{}".format(caller,e))


# General Functionality

def retInt(c):
    retVal = False

    try:
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
