f = None

caso = int(input("Tamanho do caso "))
if (caso == 11):
    f = open("testes/grid-11x11.txt", "r")
elif (caso == 15):
    f = open("testes/grid-15x15.txt", "r")
elif (caso == 25):
    f = open("testes/grid-25x25.txt", "r")

nsei = f.read()

print(nsei)
