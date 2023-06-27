from random import randint

class MLP:
    def __init__(self, neural_network):
        self.nn = neural_network

    def train(self, inputs, targets, iterations):
        for i in range(iterations):
            idx = randint(0, len(targets) - 1)
            self.nn.train(inputs[idx], [targets[idx]])

    def test(self, inputs, targets):
        acc = 0
        for i in range(len(inputs)):
            result = self.nn.predict(inputs[i])[0]
            if targets[i] == 0.0 and result < 0.25:
                acc += 1
            if targets[i] == 0.5 and result > 0.25 and result < 0.75:
                acc += 1
            if targets[i] == 1.0 and result > 0.75:
                acc += 1

        return f'{(100 * acc) / (len(targets))}%'
    
    def predict(self, inputs):
        return self.nn.predict(inputs)
