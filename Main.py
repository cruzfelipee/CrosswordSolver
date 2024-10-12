import Word
import Utilities
import Backtracking
from FileReader import FileReader
from MatrixRebuilder import MatrixRebuilder

CHOSEN_CASE = 5

reader = FileReader()
reader.readFile(CHOSEN_CASE)
matrix = reader.getMatrix()

print("solving for matrix:")

Utilities.printMatrix(matrix)

words = reader.getWords()

for word in words:
    word.updateAdjacents()

for word in words:
    print(str(word))

print("read everything, starting")

for word in Word.words:
    word.updateAdjacents()
      
Word.sortWords()

caminhamento = Backtracking.Backtracking()
caminhamento.start()

print("done")

for word in words:
    print(str(word))

matrixRebuilder = MatrixRebuilder(CHOSEN_CASE)
matrixRebuilder.rebuild(words)

for line in matrixRebuilder.m:
    print(line)
