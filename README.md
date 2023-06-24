# mlp-backpropagation
Multi-layer perceptron and backpropagation implementation and iris fisher dataset classification

# About

The current repository stores the code for an implementation of a Multi-Layer Perceptron and Backpropagation algorithm using Python.

To test the effectiveness of the implementation, I classified Iris dataset. The dataset was obtained from sklearn (scikit-learn) and it has 4 inputs: Sepal length and width, Petal length and width. As output we have the species.


# Data Treatment

The data was splitted in 70% train data and 30% test data for validation of the training. We have 4 inputs and 1 output.

The data was normalized to represent the species Vinginica, Setosa and Versicolor as 0, 0.5 and 1 in this order.


# Instructions

The problem was solved using python 3, you must have it installed!

First, clone this repository

`git clone https://github.com/brigide/missionaries-cannibals-ai-search-algorithms`

Install scikit-learn if you do not have it

`pip install scikit-learn`

Then, simply run 

`python main.py`



# Implementation

The Neural Network weights are treated as matrices, both the feed forward and backpropagation algorithms uses matrices multiplication.

All necessary matrix math was implemented without the use of libraries with the objective of revisiting some Linear Algebra concepts (optimization was not the focus).

The MLP class recieves a Neural Network as parameter and has 2 main functions: train (feed forward and backpropagation based on the error on each layer) and test (feed forward, validation of the outputs comparing with expected targets and calculation of the accuracy after the training).


# Results

2 Networks topologies were tested:

- 1 hidden layer with 4 nodes;
- 2 hidden layers with 4 and 3 nodes in this order.

This can be found in main.py file. 
