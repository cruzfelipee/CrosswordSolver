import Word
import MatrixRebuilder
import time
import collections

class Backtracking:
    def start(self):
        self.stack = collections.deque()

        for word in Word.words:
            self.stack.append(word)
            for possibleWord in word.possibleWords:
                word.text = possibleWord
                self.solve(word)
                if self.areAllWordsValid():
                    return

            return

    def solve(self, word):
        if self.areAllWordsValid():
            print("Solved board")
            return # achou solucao

        if not word.isValid():
            # print("backtracking for word: " + str(word))
            return # backtrack
        
        # mr = MatrixRebuilder.MatrixRebuilder(11)
        # mr.rebuild(Word.words)
        # mr.printMatrix()
        # time.sleep(1)

        print("Word " + str(word) + " is valid, solving for adjacents")

        for otherWord in word.adjacents.values():
            for possibleWord in otherWord.possibleWords:
                otherWord.text = possibleWord
                # otherWord.possibleWords.remove(possibleWord)
                if self.areAllWordsValid():
                    print("Solved")
                    return # achou solucao
                if not otherWord.isValid():
                    self.solve(otherWord)
        
        print("no word combination possible for " + str(word))

    def areAllWordsValid(self):
        for word in Word.words:
            if not word.isValid():
                # print("Not valid")
                return False 
        
        return True
