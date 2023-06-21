from neural_network import NeuralNetwork
from matrix import Matrix

def main():
    neural_network = NeuralNetwork(2, 2, 1)
    input = [1, 0]
    target = [1]
    # output = neural_network.feed_forward(input)

    neural_network.train(input, target)


if __name__ == '__main__':
    main()