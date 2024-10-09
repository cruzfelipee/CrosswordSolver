import Utilities
import Caminhamento
from FileReader import FileReader

reader = FileReader()
reader.readFile(int(input("Tamanho do caso ")))
matrix = reader.getMatrix()

Utilities.printMatrix(matrix)

# inicializa os objetos da classe Word
reader.getHorizontal()
reader.getVertical()

print("read everuythonmg")

# possible_words = reader.getPossibleWords()
# print(f"Possible words: {len(possible_words)}")

print("strting")

caminhamento = Caminhamento.Caminhamento()
caminhamento.start()


