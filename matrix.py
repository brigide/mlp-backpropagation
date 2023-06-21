from random import uniform
import numpy as np

class Matrix:
    """Simple Matrix operations lib"""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for col in range(cols)] for row in range(rows)]

    @staticmethod
    def from_array(array):
        m = Matrix(len(array), 1)
        for i in range(len(array)):
            m.data[i][0] = array[i]

        return m
    
    @staticmethod
    def from_number(n):
        m = Matrix(1, 1)
        m.data[0][0] = n

        return m
    
    def to_array(self):
        array = []
        for i in range(self.rows):
            for j in range(self.cols):
                array.append(self.data[i][j])

        return array


    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = uniform(-1, 1)


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
    def subtract(m, n):
        # scalar
        for i in range(m.rows):
            for j in range(m.cols):
                m.data[i][j] -= n.data[i][j]

        return m

    def multiply_hamard(self, n):
        # element wise
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n.data[i][j]

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

    @staticmethod
    def static_map(m, fn):
        matrix = Matrix(m.rows, m.cols)
        # apply a function to every element of the matrix
        for i in range(m.rows):
            for j in range(m.cols):
                val = m.data[i][j]
                matrix.data[i][j] = fn(val)

        return matrix

    def log(self):

        # Do heading
        print("     ", end="")
        for j in range(len(self.data[0])):
            print("%5d " % j, end="")
        print()
        print("     ", end="")
        for j in range(len(self.data[0])):
            print("------", end="")
        print()
        # Matrix contents
        for i in range(len(self.data)):
            print("%3d |" % (i), end="") # Row nums
            for j in range(len(self.data[0])):
                print("%.2f " % (self.data[i][j]), end="")
            print()  