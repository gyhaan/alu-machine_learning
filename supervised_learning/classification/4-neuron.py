#!/usr/bin/env python3
"""Module that defines a single neuron performing binary classification."""
import numpy as np


class Neuron:
    """A single neuron performing binary classification."""

    def __init__(self, nx):
        """
        Initializes the neuron.

        Args:
            nx (int): The number of input features to the neuron.

        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        # Initialize private attributes
        self.__W = np.random.randn(1, nx)
        self.__b = 0  # Bias (initialized to 0)
        self.__A = 0  # Activated output (initialized to 0)

    @property
    def W(self):
        """Getter for the weights vector."""
        return self.__W

    @property
    def b(self):
        """Getter for the bias."""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output."""
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron.

        Args:
            X (numpy.ndarray): Input data with shape (nx, m),
                               where nx is the number of input features,
                               and m is the number of examples.

        Returns:
            numpy.ndarray: The activated output of the neuron.
        """
        # Linear transformation
        Z = np.dot(self.__W, X) + self.__b

        # Sigmoid activation
        self.__A = 1 / (1 + np.exp(-Z))

        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression.

        Args:
            Y (numpy.ndarray): Correct labels for the input data
            with shape (1, m).
            A (numpy.ndarray): Activated output of the neuron
            for each example with shape (1, m).

        Returns:
            float: The cost of the model.
        """
        m = Y.shape[1]  # Number of examples

        # Compute cost using logistic regression cost function
        cost = -(1 / m) * np.sum(Y * np.log(A) +
                                 (1 - Y) * np.log(1.0000001 - A))

        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions.

        Args:
            X (numpy.ndarray): Input data with shape (nx, m),
                               where nx is the number of input features,
                               and m is the number of examples.
            Y (numpy.ndarray): Correct labels for the input data with
              shape (1, m).

        Returns:
            tuple: The neuron’s prediction and the cost of the network.
                - prediction: numpy.ndarray with shape (1, m)
                  containing the predicted labels (1 if >= 0.5, else 0).
                - cost: float representing the cost of the network.
        """
        # Perform forward propagation to calculate predictions
        A = self.forward_prop(X)

        # Generate predictions: 1 if A >= 0.5, else 0
        prediction = np.where(A >= 0.5, 1, 0)

        # Compute the cost
        cost = self.cost(Y, A)

        return prediction, cost
