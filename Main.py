import Utilities
import Caminhamento
from FileReader import FileReader
from MatrixRebuilder import MatrixRebuilder

CHOSEN_CASE = 5

reader = FileReader()
reader.readFile(CHOSEN_CASE)
matrix = reader.getMatrix()

Utilities.printMatrix(matrix)

# inicializa os objetos da classe Word
# reader.getHorizontal()
# reader.getVertical()

words = reader.getWords()

for word in words:
    word.updateAdjacents()

for word in words:
    print(str(word))
    print(len(word.possibleWords))

print("read everything")

# possible_words = reader.getPossibleWords()
# print(f"Possible words: {len(possible_words)}")

print("starting")

caminhamento = Caminhamento.Caminhamento()
for i in range(len(words)):
    print(f"Starting thread {i}")
    caminhamento.start()
    

print("done")

for word in words:
    print(str(word))

matrixRebuilder = MatrixRebuilder(CHOSEN_CASE)
matrixRebuilder.rebuild(words)

for line in matrixRebuilder.m:
    print(line)
