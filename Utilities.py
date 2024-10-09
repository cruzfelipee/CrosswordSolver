def printMatrix(m):
    for i in m:
        print(i.strip())

def getMaxLenWord(word_list):
    maxLen = 0
    for i in word_list:
        if i.getLen() > maxLen:
            maxLen = i.getLen()
    return maxLen

def getMinLenWord(word_list):
    minLen = 10000000000000
    for i in word_list:
        if i.getLen() < minLen:
            minLen = i.getLen()
    return minLen