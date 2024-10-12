import Word
import random

class Caminhamento:
    def start(self):
        while not self.areAllWordsValid():
            self.refine()

    def refine(self):
        # Word.sortWords()

        for word in Word.words:
            # print(str(word) + " is valid")
            if word.isValid():
                print(str(word) + " is valid")
                continue
           #elif not word.isValid():
                #print(str(word) + " is not valid")

            # (nao valido) ou (? na palavra)

            #print("randomizing " + str(word))
            word.text = random.choice(word.possibleWords)

            return

    def areAllWordsValid(self):
        for word in Word.words:
            if not word.isValid():
                # print("Not valid")
                return False 
        
        return True
    
    def startOLD(self):
        totalValid = True
        for word in Word.words:
            valid = False
            if word.isValid() and not ("?" in word.text):
                valid = True
                continue # se a palavra ja for valida, vai para a proxima

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
                    valid = True
                    print(word.text)
                    break # se a palavra for valida, sai do loop
            
            totalValid = totalValid and valid #alterado com o totalValid
        
        return totalValid
