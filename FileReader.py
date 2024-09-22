from Word import Word
from Position import Position

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

    def getHorizontal(self):
        words = []

        for y in range(len(self.matrix)):
            word = Word("", "Horizontal")
            for x in range(len(self.matrix[y])):
                character = self.matrix[y][x]
                if character == "." and word.text != "":
                    word.Position = Position(x, y)
                    words.append(word) # adds current word to graph
                    word = Word("", "Horizontal") # resets word
                else:
                    word.text += character #acumulates characters
            # adds the words when line breaks
            word.Position = Position(len(self.matrix.y), y)
            words.append(word) # adds current word to graph
            word = Word("", "Horizontal") # resets word
        
        return words
