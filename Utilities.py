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
