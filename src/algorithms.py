# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithms.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/23 21:02:09 by obelouch          #+#    #+#              #
#    Updated: 2020/12/23 21:02:09 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.math import sigmoid
import numpy as np

# Max Iteration Macro:
MAX_ITER = 10000


def     bgd(X, Y):
    '''
    Apply the Batch Gradient Descent 
    '''
    # Learning Rate
    alpha = 0.5
    # Init Theta
    theta = np.zeros((9, 1))
    # Launch the Gradient Algorithm
    for _ in range(MAX_ITER):
        h = sigmoid(X.dot(theta))
        theta -= alpha * np.transpose(X).dot(h - Y) / Y.shape[0]
    # Rehape theta to a simple vector before return it
    theta = np.reshape(theta, (9,))
    return theta


def     sgd(X, Y):
    '''
    Apply the Stochastic Gradient Descent
    '''
    # Learning Rate
    alpha = 0.5
    # Init Theta
    theta = np.zeros((9, 1))
    m = Y.shape[0]
    n = 9
    # Launch the Gradient Algorithm
    for _ in range(20):
        for i in range(m):
            for j in range(n):
                h = sigmoid((X[i]).dot(theta))
                theta[j] -= (alpha / m) * (h - Y[i]) * X[i][j]
    # Rehape theta to a simple vector before return it
    theta = np.reshape(theta, (9,))
    return theta
