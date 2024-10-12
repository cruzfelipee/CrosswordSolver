import Word

# self = this

class Backtracking:
    def start(self):
        for word in Word.words:
            for possibleWord in word.possibleWords:
                word.text = possibleWord
                self.solve(word)
                if self.areAllWordsValid():
                    return

            return

    def solve(self, word):
        if self.areAllWordsValid() and not ('?' in word.text):
            print("Solved")
            return # achou solucao

        if not word.isValid() and not ('?' in word.text):
            #print("backtracking for word: " + str(word))
            return # backtrack

        for otherWord in word.adjacents.values():
            for possibleWord in otherWord.possibleWords:
                otherWord.text = possibleWord
                if self.areAllWordsValid() and not ('?' in word.text):
                    print("Solved")
                    return # achou solucao
                self.solve(otherWord)

    def areAllWordsValid(self):
        for word in Word.words:
            if not word.isValid() or ('?' in word.text):
                # print("Not valid")
                return False 
        
        return True