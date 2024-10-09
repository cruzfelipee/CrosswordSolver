import Word

class Caminhamento:
    def start(self):
        for word in Word.words:
            word.updateAdjacents()
        
        Word.sortWords()
        
        for word in Word.words:
            for possibleWord in word.possibleWords:
                word.text = possibleWord
                if word.isValid():
                    break # se a palavra for valida, sai do loop
        
        print("Done")
