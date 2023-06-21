from neural_network import NeuralNetwork
from matrix import Matrix
from random import randint

def main():
    neural_network = NeuralNetwork(2, 2, 1)
    inputs = [[1, 0], [0, 1], [1, 1], [0, 0]]
    targets = [[1], [1], [0], [0]]

    for i in range(100000):
        idx = randint(0, 3)
        neural_network.train(inputs[idx], targets[idx])

    print(neural_network.predict([1, 0]))
    print(neural_network.predict([1, 1]))
    print(neural_network.predict([0, 1]))
    print(neural_network.predict([0, 0]))



if __name__ == '__main__':
    main()