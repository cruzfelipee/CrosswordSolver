from Position import Position

class Word:
    # esse sinal de igual (=) depois de startPoint atribui um valor default, entao se tu n passar nada qnd instancia Word, ele recebe None
    def __init__(self, text  : str, type : str, endPosition : Position = None) -> None:
        self.text = text # the actual word
        self.type = type # horizontal/vertical
        self.startPoint = endPosition # position in matrix of the last character of the word

    def __str__(self) -> str:
        return f"Text: {self.text}; Type: {self.type}; StartPoint: {self.startPoint}"
