import Word

class MatrixRebuilder:
    def __init__(self, size):
        self.m = [["." for _ in range(size)] for _ in range(size)]

    def rebuild(self, words):
        for word in words:
            i = 0
            if word.wordType == "Horizontal":
                for letter in (word.text):
                    self.m[word.startPosition.y][word.startPosition.x + i] = letter
                    i += 1
            else:
                for letter in (word.text):
                    self.m[word.startPosition.y + i][word.startPosition.x] = letter
                    i += 1
    
    def printMatrix(self):
        for line in self.m:
            print(line)