#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    hiddenlist = dir(hidden_4)
    for i in range(len(hiddenlist)):
        if (hiddenlist[i][0] != "_"):
            print(hiddenlist[i])
