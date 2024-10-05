from Position import Position

class Word:
    # esse sinal de igual (=) depois de startPoint atribui um valor default, entao se tu n passar nada qnd instancia Word, ele recebe None
    def __init__(self, text  : str, wordType : str, startPosition : Position = None) -> None:
        self.text = text # the actual word
        self.wordType = wordType # horizontal/vertical
        self.startPosition = startPosition # position in matrix of the last character of the word

    def __str__(self) -> str:
        return f"[Text: {self.text}; Type: {self.wordType}; StartPosition: {self.startPosition}]"

    def getLen(self):
        return len(self.text)