class Position:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"[X = {self.x}; Y = {self.y}]"
