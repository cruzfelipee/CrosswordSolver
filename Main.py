import Utilities
from FileReader import FileReader

reader = FileReader()
reader.readFile(int(input("Tamanho do caso ")))
matrix = reader.getMatrix()

Utilities.printMatrix(matrix)

for word in reader.getHorizontal():
    print(str(word))
