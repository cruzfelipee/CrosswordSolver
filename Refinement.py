import Word
import random

class Refinement:
    def start(self):
        while not self.areAllWordsValid():
            self.refine()

    def refine(self):
        # Word.sortWords()

        for word in Word.words:
            # print(str(word) + " is valid")
            if word.isValid():
                #print(str(word) + " is valid")
                continue
           #elif not word.isValid():
                #print(str(word) + " is not valid")

            # (nao valido) ou (? na palavra)

            #print("randomizing " + str(word))
            realPossibleWords = []
            for possibleWord in word.possibleWords:
                word.text = possibleWord
                if word.isValid():
                    realPossibleWords.append(possibleWord)

            if len(realPossibleWords) == 0:
                continue

            word.text = random.choice(realPossibleWords)

            return

    def areAllWordsValid(self):
        for word in Word.words:
            if not word.isValid():
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
                
                word.text = possibleWord
                if word.isValid() and not ("?" in word.text):
                    valid = True
                    print(word.text)
                    break # se a palavra for valida, sai do loop
            
            totalValid = totalValid and valid #alterado com o totalValid
        
        return totalValid
