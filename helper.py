import numpy as np
from collections import Counter


def load_data():
    """
    load dataset from reviews and labels text files
    :return (list of reviews , list of reviews labels):
    """
    with open('dataset/reviews.txt') as reviews_file:
        reviews = list(map(lambda line: line[:-1], reviews_file.readlines()))
    if reviews is None:
        raise FileNotFoundError("there is a problem reading reviews file")
    with open('dataset/labels.txt') as labels_file:
        labels = list(map(lambda line: line[:-1], labels_file.readlines()))
    if labels is None:
        raise FileNotFoundError("there is a problem reading labels file")
    return reviews, labels


def max_counter_value(counter: Counter):
    mx = -np.inf
    for value in counter.values():
        mx = max(mx, value)
    return mx


def min_counter_value(counter: Counter):
    mn = np.inf
    for value in counter.values():
        mn = min(mn, value)
    return mn


class NNLiner:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        self.values = np.zeros((1,output_size), float)

        std = self.input_size ** -0.5
        self.weights = np.random.normal(0.0, std, (self.input_size, self.output_size))

        self.bias = np.zeros((1,self.output_size), float)

    def __call__(self, x):
        self.values = np.dot(x, self.weights) + self.bias
        return self.values
