from neural_network import NeuralNetwork
from matrix import Matrix

def main():
    neural_network = NeuralNetwork(2, 2, 1)
    input = [1, 0]
    output = neural_network.feed_forward(input)

    print(output)


if __name__ == '__main__':
    main()