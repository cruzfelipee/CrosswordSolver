from Word import Word
from Position import Position
import Utilities
import numpy as np

class FileReader:
    def __init__(self) -> None:
        pass

    # returns the read file as matrix
    def getMatrix(self):
        self.matrix = self.file.readlines()
        # for line in self.matrix:
        #     line.replace("\n", "")
        for i in range(len(self.matrix)):
            self.matrix[i] = self.matrix[i].replace("\n", "")
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
                    lastIndex = find + len(text)
        
        return words

    def getVertical(self):
        np_matrix = np.array([list(row) for row in self.matrix])
        aux_matrix = self.matrix.copy()
        self.matrix = np_matrix.T.tolist()
        self.matrix = ["".join(row) for row in self.matrix]
        r = self.getHorizontal("Vertical")
        self.matrix = aux_matrix
        return r

    def getWords(self):
        return self.getHorizontal() + self.getVertical()

    def getPossibleWords(self):
        words = self.getWords()
        max_len = Utilities.getMaxLenWord(words)
        min_len = Utilities.getMinLenWord(words)
        possible_words = []

        with open("lista_palavras.txt", "r") as file:
            for line in file:
                if len(line) >= min_len and len(line) <= max_len:
                    possible_words.append(line.strip())
        
        return possible_words