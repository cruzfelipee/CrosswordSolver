from Position import Position
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
        self.endPosition = Position(startPosition.x + len(text) - 1, startPosition.y) if wordType == "Horizontal" else Position(startPosition.x, startPosition.y + len(text) - 1)
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
    
    def isValid(self, text : str = None) -> bool:
        """
        retorna True se, de todas as palavras adjacentes as letras são compatíveis
        """

        if text == None:
            text = self.text

        if ("?" in text): #or self.isWordAlreadyInUse():
            return False # se a palavra ja foi usada, nao pode ser usada de novo

        for index in self.adjacents.keys():
            # position é a posicao de interseccao com a palavra adjacente
            otherWord = self.adjacents[index]

            if "?" in otherWord.text:
                continue # se a palavra adjacente ainda, entao respeita a restricao
            
            changed = False
            otherIndex = 0
            for key, value in otherWord.adjacents.items():
                if value == self:
                    otherIndex = key
                    changed = True
                    break
            
            if not changed: # aaq
                print("Error: otherIndex not found")

            if text[index] != otherWord.text[otherIndex]:
                return False # nao encaixa com a palavra adjacente
        
        return True # nenhuma restricao foi violada
            
    def isWordAlreadyInUse(self) -> bool:
        for word in words:
            if word.text == self.text and not "?" in self.text:
                return True
        return False
    
