# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/23 00:37:11 by obelouch          #+#    #+#              #
#    Updated: 2020/12/23 00:44:31 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.math import sigmoid
import numpy as np

# Houses Names:
houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']


def     h(Theta, X):
    '''
    Hypothesis finction
    '''
    return sigmoid(X.dot(Theta))


def     prediction(Theta, X):
    '''
    Return a vector of Predicted Houses
    '''
    # Prediction Matrice:
    predict_matrice = h(Theta, X)
    # Get the max column index of each row
    prediction = []
    for i in range(X.shape[0]):
        prediction.append(
            houses[np.argmax(predict_matrice[i])]
        )
    return prediction


def     get_Y(labels, house):
    '''
    Create the One vs All Ys
    '''
    Y = np.array([int(y == house) for y in labels], ndmin=2)
    return np.transpose(Y)


def     get_dict_Y(labels):
    '''
    Take a predict houses labels and return a dictionary classify
    for each house
    '''
    return {
        'G': get_Y(labels, 'Gryffindor'),
        'R': get_Y(labels, 'Ravenclaw'),
        'H': get_Y(labels, 'Hufflepuff'),
        'S': get_Y(labels, 'Slytherin'),
    }