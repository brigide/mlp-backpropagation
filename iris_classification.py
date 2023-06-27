from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from mlp import MLP
from neural_network import NeuralNetwork


def normalize_target(y):
    arr = []
    for i in range(len(y)):
        arr.append(y[i]/ 2)
    return arr


def main():
    iris = datasets.load_iris()
    x, y = iris.data, iris.target

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

    y_train = normalize_target(y_train)
    y_test = normalize_target(y_test)

    iris_1 = MLP(NeuralNetwork(4, 3, 1))
    iris_1.train(x_train, y_train, 5000)
    acc1 = iris_1.test(x_test, y_test)

    iris_2 = MLP(NeuralNetwork(4, 4, 3, 1))
    iris_2.train(x_train, y_train, 5000)
    acc2 = iris_2.test(x_test, y_test)

    print(f'1 hidden layer with 4 nodes:             {acc1}')
    print(f'2 hidden layer with 4 nodes and 3 nodes: {acc2}')


main()