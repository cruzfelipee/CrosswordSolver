import Word
import Utilities
import Backtracking2
import Refinement
from FileReader import FileReader
from MatrixRebuilder import MatrixRebuilder
import MatrixVisualizer

CHOSEN_CASE = 11

reader = FileReader()
reader.readFile(CHOSEN_CASE)
matrix = reader.getMatrix()

print("solving for matrix:")

Utilities.printMatrix(matrix)

words = reader.getWords()

for word in words:
    word.updateAdjacents()

print("words from file reader:")
for word in words:
    print(str(word))

print("read everything, starting")

for word in Word.words:
    word.updateAdjacents()
      
Word.sortWords()

# caminhamento = Backtracking2.Backtracking()
# caminhamento.start()

caminhamento = Refinement.Refinement()
caminhamento.start()

print("done")

for word in words:
    print(str(word))

matrixRebuilder = MatrixRebuilder(CHOSEN_CASE)
matrixRebuilder.rebuild(words)

print("reconstructed matrix:")
for line in matrixRebuilder.m:
    print(line)

MatrixVisualizer.visualizeMatrix(matrixRebuilder.m)
