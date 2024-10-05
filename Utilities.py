def printMatrix(m):
    for i in m:
        print(i.strip())

def replaceCharacter(s : str, index : int, character : str):
    pass #da replace no cahracter

def invertMatrix(m):
    for x in range(len(m)):
        for y in range(len(m[x])):
            aux = m[x][y]
            m[x][y] = m[y][x] # troca essas 2 linhas pelo replacecharacter
            m[y][x] = aux

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