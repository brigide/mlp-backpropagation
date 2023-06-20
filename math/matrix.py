from random import uniform

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = []

        for i in range(self.rows):
            self.values[i] = []
            for j in range(self.cols):
                self.values[i][j] = 0

    def randomize(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] = uniform(0, 10)

    def multiply(self, n):
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] *= n.values[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] *= n

    def add(self, n):
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] += n.values[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] += n