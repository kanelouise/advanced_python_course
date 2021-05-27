class Square:
    def __init__(self, val=2):
        self.counterval = val

    def squareme(self):
        self.counterval = self.counterval ** 2

    def getme(self):
        return self.counterval


