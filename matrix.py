from random import uniform
import numpy as np

class Matrix:
    """Simple Matrix operations lib"""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for col in range(cols)] for row in range(rows)]

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = uniform(0, 10)


    @staticmethod
    def multiply_matrix(m, n):
        # matrix product
        if m.cols != n.rows:
            return None # cols of self must match rows of n
        
        result = Matrix(m.rows, n.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(m.cols):
                    sum += m.data[i][k] * n.data[k][j]

                result.data[i][j] = sum

        return result

    def multiply_scalar(self, n):
        # scalar
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n

    @staticmethod
    def transpose(m):
        result = Matrix(m.cols, m.rows)
        for i in range(m.rows):
            for j in range(m.cols):
                result.data[j][i] = m.data[i][j]

        return result

    def add(self, n):
        # element wise
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n.data[i][j]
        # scalar
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n

    def map(self, fn):
        # apply a function to every element of the matrix
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = fn(val)

    def log(self):
        print(np.matrix(self.data))