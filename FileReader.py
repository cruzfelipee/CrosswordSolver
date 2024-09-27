from Word import Word
from Position import Position
import Utilities

class FileReader:
    def __init__(self) -> None:
        pass

    # returns the read file as matrix
    def getMatrix(self):
        self.matrix = self.file.readlines()
        for line in self.matrix:
            line.replace("\n", "")
        return self.matrix

    # reads the specified case
    def readFile(self, case : int):
        self.file = open(f"testes/grid-{case}x{case}.txt", "r")

    def getHorizontal(self, wordType : str = "Horizontal"):
        words = []

        for y in range(len(self.matrix)):
            line : str = self.matrix[y]
            splitWords = line.split(".") # divide a linha com os pontos
            
            lastIndex = 0
            for text in splitWords:
                if len(text) > 2:
                    find = line.find(text, lastIndex)
                    pos = Position(find, y) if wordType == "Horizontal" else Position(y, find)
                    words.append(Word(text.strip(), wordType, pos))
                    lastIndex = find
        
        return words

    def getVertical(self):
        Utilities.invertMatrix(self.matrix) # inverte, pq dai coluna vira linha e vice versa
        return self.getHorizontal("Vertical")
        Utilities.invertMatrix(self.matrix) # reverte pra nao estragar o resto do codigo
