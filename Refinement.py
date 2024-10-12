import Word
import random

class Refinement:
    def start(self):
        while not self.areAllWordsValid():
            self.refine()

    def refine(self):
        # pra cada palavra
        for word in Word.words:
            if word.isValid(): # se a palavra ja for valida, vai para a proxima
                continue

            realPossibleWords = [possibleWord for possibleWord in word.possibleWords if word.isValid(possibleWord)] # lista de palavras possiveis que sao validas de verdade
            # for possibleWord in word.possibleWords:
            #     word.text = possibleWord
            #     if word.isValid():
            #         realPossibleWords.append(possibleWord)

            if len(realPossibleWords) == 0:
                continue

            word.text = random.choice(realPossibleWords) # escolhe uma palavra valida aleatoria que caiba e seja valida

            return

    def areAllWordsValid(self):
        for word in Word.words:
            if not word.isValid():
                return False 
        
        return True
