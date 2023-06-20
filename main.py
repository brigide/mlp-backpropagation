from neural_network import NeuralNetwork
from matrix import Matrix

def doubleIt(x):
    return x * 2

def main():
    NeuralNetwork(1, 2, 4, 5, 3)
    m1 = Matrix(2, 2)
    m1.randomize()
    m1.log()
    m1.map(doubleIt)
    m1.log()



if __name__ == '__main__':
    main()