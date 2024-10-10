import Word

class Caminhamento:
    def start(self):
        for word in Word.words:
            word.updateAdjacents()
        
        Word.sortWords()
        
        for word in Word.words:
            for possibleWord in word.possibleWords:
                """
                    Não pode ser assim, num exemplo:

                            casa
                              ?
                              ?
                              ?

                    Se a gente só atribuir o valor de possibleWord, ele pode substituir o "s", se tentar
                    atribuir a palavra "caro", por exemplo, e aí a palavra "casa" viraria "caca", o que
                    não é válido.

                    O certo seria, a cada atribuição de uma palvra, recalcular as palavras possíveis 

                """
                
                word.text = possibleWord
                if word.isValid() and not ("?" in word.text):
                    break # se a palavra for valida, sai do loop
        
        print("Done")
