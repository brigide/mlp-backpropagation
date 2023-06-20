class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = []

        for i in range(self.rows):
            self.values[i] = []
            for j in range(self.cols):
                self.values[i][j] = 0

    def multiply(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] *= n

    def add(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] += n