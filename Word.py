from Position import Position
import Utilities
words = []

def sortWords(): # ordena array words do maior numero de restricoes pro menor
    words.sort(key = lambda x: x.getNumberOfAdjacents(), reverse = True)

def getWordsOfSize(size):
        possible_words = []

        with open("lista_palavras.txt", "r", encoding="utf8") as file:
            for line in file:
                if len(line) == size:
                    possible_words.append(line.strip())
        
        return possible_words


class Word:
    all_words = [line.strip() for line in open("lista_palavras.txt", "r")]
    # esse sinal de igual (=) depois de startPoint atribui um valor default, entao se tu n passar nada qnd instancia Word, ele recebe None
    def __init__(self, text  : str, wordType : str, startPosition : Position = None) -> None:
        self.text = text # the actual word
        self.wordType = wordType # horizontal/vertical
        self.startPosition = startPosition # position in matrix of the last character of the word
        self.endPosition = Position(startPosition.x + len(text), startPosition.y) if wordType == "Horizontal" else Position(startPosition.x, startPosition.y + len(text))
        self.possibleWords = [word for word in Word.all_words if len(word) == len(text)]
        self.adjacents = {}
        self.updateAdjacents()
        words.append(self)

    def __str__(self) -> str:
        return f"[Text: {self.text}; Type: {self.wordType}; StartPosition: {self.startPosition}; Adjacent: {', '.join(f'{key} -> {str(adj)}' for key, adj in self.adjacents.items())}]"

    def __len__(self):
        return len(self.text)
    
    def updateAdjacents(self):
        for otherWord in words:
            if otherWord.wordType == self.wordType:
                continue # palavras horiontais so podem cruzar verticais e vice versa
            
            if self.wordType == "Vertical":
                if self.startPosition.x >= otherWord.startPosition.x and self.startPosition.x <= otherWord.endPosition.x:
                    if self.startPosition.y <= otherWord.startPosition.y and self.endPosition.y >= otherWord.startPosition.y:
                        self.adjacents[otherWord.startPosition.y] = otherWord
            else:
                if self.startPosition.y >= otherWord.startPosition.y and self.startPosition.y <= otherWord.endPosition.y:
                    if self.startPosition.x <= otherWord.startPosition.x and self.endPosition.x >= otherWord.startPosition.x:
                        self.adjacents[otherWord.startPosition.x] = otherWord
    
    def getNumberOfAdjacents(self):
        return len(self.adjacents)
    
    # sei la oq ta acontecendo nesse metodo help
    def isValid(self) -> bool: # true se respeita a restricao
        for position in self.adjacents.keys():
            otherWord = self.adjacents[position]
            otherIndex = self.startPosition.y if self.wordType == "Horizontal" else self.startPosition.x
            relativePos = otherIndex - otherWord.startPosition.x if self.wordType == "Horizontal" else otherWord.startPosition.y
            # print(f"Checking: self.text[{position}] vs otherWord.text[{relativePos}]")
            # print(f"self.text: {self.text}, otherWord.text: {otherWord.text}")

            if self.text[position] != otherWord.text[relativePos]:
                return False

        return True