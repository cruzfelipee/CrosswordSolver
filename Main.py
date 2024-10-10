import Utilities
import Caminhamento
from FileReader import FileReader

reader = FileReader()
reader.readFile(11)
matrix = reader.getMatrix()

Utilities.printMatrix(matrix)

# inicializa os objetos da classe Word
# reader.getHorizontal()
# reader.getVertical()

words = reader.getWords()

for word in words:
    print(str(word))
    print(len(word.possibleWords))

print("read everuythonmg")

# possible_words = reader.getPossibleWords()
# print(f"Possible words: {len(possible_words)}")

print("strting")

caminhamento = Caminhamento.Caminhamento()
caminhamento.start()

print("done")

for word in words:
     print(str(word))


