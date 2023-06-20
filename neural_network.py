class NeuralNetwork:
    """Neural Network class"""
    def __init__(self, *arg):
        """Constructor accepts any number of arguments
            first argument being number of inputs
            middle arguments being hidden layers number of nodes,
            last being number of outputs"""
        if len(arg) < 2:
            return 'at least 2 arguments are necessary'
        
        self.input_nodes = arg[1]
        self.output_nodes = arg[-1]

        self.hidden_nodes = [n for n in arg[1:-1]]

        