from Position import Position
import Utilities
words = []

def sortWords(): # ordena array words do maior numero de restricoes pro menor
    words.sort(key = lambda x: x.getNumberOfAdjacents(), reverse = True)

def getWordsOfSize(size):
        possible_words = []

        with open("lista_palavras.txt", "r", encoding="utf8") as file:
            for line in file:
                if len(line.strip()) == size and not ("?" in line):
                    possible_words.append(line.strip())
        
        return possible_words


class Word:
    all_words = [line.strip() for line in open("lista_palavras.txt", "r", encoding="utf8")]
    # esse sinal de igual (=) depois de startPoint atribui um valor default, entao se tu n passar nada qnd instancia Word, ele recebe None
    def __init__(self, text  : str, wordType : str, startPosition : Position = None) -> None:
        self.text = text # the actual word
        self.wordType = wordType # horizontal/vertical
        self.startPosition = startPosition # position in matrix of the last character of the word
        self.endPosition = Position(startPosition.x + len(text), startPosition.y) if wordType == "Horizontal" else Position(startPosition.x, startPosition.y + len(text))
        self.possibleWords = getWordsOfSize(len(text))
        self.adjacents = {}
        # self.updateAdjacents() n faz sentido chamar antes de todas as palavras estarem criadas
        words.append(self)

    def __str__(self) -> str:
        return f"[Text: {self.text}; Type: {self.wordType}; StartPosition: {str(self.startPosition)}; Adjacent: {', '.join(f'{key} -> {str(adj.text)}' for key, adj in self.adjacents.items())}]"

    def __len__(self):
        return len(self.text)
    
    def updateAdjacents(self):
        for otherWord in words:
            if otherWord.wordType == self.wordType:
                continue # palavras horiontais so podem cruzar verticais e vice versa
            
            if self.wordType == "Vertical":
                if self.startPosition.x >= otherWord.startPosition.x and self.startPosition.x <= otherWord.endPosition.x:
                    if self.startPosition.y <= otherWord.startPosition.y and self.endPosition.y >= otherWord.startPosition.y:
                        self.adjacents[otherWord.startPosition.y - self.startPosition.y] = otherWord
            else:
                if self.startPosition.y >= otherWord.startPosition.y and self.startPosition.y <= otherWord.endPosition.y:
                    if self.startPosition.x <= otherWord.startPosition.x and self.endPosition.x >= otherWord.startPosition.x:
                        self.adjacents[otherWord.startPosition.x - self.startPosition.x] = otherWord
    
    def getNumberOfAdjacents(self):
        return len(self.adjacents)
    
    def isValid(self) -> bool:
        """
        retorna True se, de todas as palavras adjacentes as letras são compatíveis
        """
        if ("?" in self.text): #or self.isWordAlreadyInUse():
            return False # se a palavra ja foi usada, nao pode ser usada de novo

        for index in self.adjacents.keys():
            # position é a posicao de interseccao com a palavra adjacente
            otherWord = self.adjacents[index]

            if "?" in otherWord.text:
                continue # se a palavra adjacente ainda, entao respeita a restricao
            
            #otherIndex = otherWord.startPosition.x - self.startPosition.x if self.wordType == "Vertical" else otherWord.startPosition.y - self.startPosition.y
            changed = False
            otherIndex = 0
            for key, value in otherWord.adjacents.items():
                if value == self:
                    # print(str(otherWord) + " crosses " + str(self) + " at " + str(key))
                    otherIndex = key
                    changed = True
                    break
            
            if not changed: # aaq
                print("Error: otherIndex not found")
            
            if index >= len(self.text):
                #print("Error: index out of bounds for word " + str(self))
                continue # se as palavras nunca foram adjacentes, nao precisa verificar

            if otherIndex >= len(otherWord.text):
                #print("Error: otherIndex out of bounds for word " + str(otherWord))
                continue # se as palavras nunca foram adjacentes, nao precisa verificar

            if self.text[index] != otherWord.text[otherIndex]:
                return False # nao encaixa com a palavra adjacente
        
        return True # nenhuma restricao foi violada
            
    def isWordAlreadyInUse(self) -> bool:
        for word in words:
            if word.text == self.text and not "?" in self.text:
                #print(f"Word {self.text} is already in use")
                return True
        return False
    
    # # sei la oq ta acontecendo nesse metodo help
    # def isValid(self) -> bool: # true se respeita a restricao
    #     for position in self.adjacents.keys():
    #         otherWord = self.adjacents[position]
    #         if "?" in otherWord.text:
    #             return True # se a palavra adjacente ainda não foi definida, entao respeita a restricao
            
    #         myIndex = position - self.startPosition.y if self.wordType == "Vertical" else position - self.startPosition.x
    #         otherIndex = self.startPosition.x - otherWord.startPosition.x if self.wordType == "Vertical" else self.startPosition.y - otherWord.startPosition.y
    #         print(f"Checking: self.text[{myIndex}] vs otherWord.text[{otherIndex}]")
    #         print(f"self.text: {self.text}, otherWord.text: {otherWord.text}")

    #         if self.text[myIndex] != otherWord.text[otherIndex]:
    #             print(f"Invalid: {self.text[myIndex]} vs {otherWord.text[otherIndex]}")
    #             return False
    #     print("Valid")
    #     return True

    # def updatePossibleWords(self, word):
    #     if self.wordType == "Vertical":
    #         # cruzamento no eixo x
    #         otherIndex = self.startPosition.x - word.startPosition.x
    #         myIndex = word.startPosition.y - self.startPosition.y
    #     else:
    #         # cruzamento no eixo y
    #         otherIndex = self.startPosition.y - word.startPosition.y
    #         myIndex = word.startPosition.x - self.startPosition.x

    #     print(f"Updating: {str([self.startPosition])} vs {str(word)}")
    #     print(f"Updating: self.text[{myIndex}] vs word.text[{otherIndex}]")
    #     print(f"self.text: {self.text}, word.text: {word.text}")

    #     letter = word.text[otherIndex]
    #     self.possibleWords = [word for word in self.possibleWords if word[myIndex] == letter]
