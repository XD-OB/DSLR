# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    precision.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/21 17:41:37 by obelouch          #+#    #+#              #
#    Updated: 2020/12/21 17:41:37 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

################################################################################
#                                                                              #
# Precision-recall evaluation metrics are effectif against a problem called:   #
# 'skewed dataset' (no balance in datset)                                      #
# https://towardsdatascience.com/a-complete-understanding-of-precision-recall- #
# and-f-score-concepts-23dc44defef6                                            #
#                                                                              #
################################################################################

from mylib.math import ft_sum, sigmoid
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

def     calcul_TP(Y, Y_pred):
    '''
    Calculate True Positive
    '''
    return ft_sum([int(y * y_pred) for y, y_pred in zip(Y, Y_pred)])


def     calcul_TN(Y, Y_pred):
    '''
    Calculate True Negative
    '''
    return ft_sum([int(y == y_pred == 0) for y, y_pred in zip(Y, Y_pred)])


def     calcul_FP(Y, Y_pred):
    '''
    Calculate True Negative
    '''
    return ft_sum([int(y == 0 and y_pred == 1) for y, y_pred in zip(Y, Y_pred)])


def     calcul_FN(Y, Y_pred):
    '''
    Calculate True Negative
    '''
    return ft_sum([int(y == 1 and y_pred == 0) for y, y_pred in zip(Y, Y_pred)])


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


def     calcul_confusionDict(Y, Y_pred):
    '''
    Confusion Matrix (as dictionnary)
    '''
    TP = calcul_TP(Y['G'], Y_pred['G']) + calcul_TP(Y['R'], Y_pred['R']) + calcul_TP(Y['H'], Y_pred['H']) + calcul_TP(Y['S'], Y_pred['S'])
    TN = calcul_TN(Y['G'], Y_pred['G']) + calcul_TN(Y['R'], Y_pred['R']) + calcul_TN(Y['H'], Y_pred['H']) + calcul_TN(Y['S'], Y_pred['S'])
    FP = calcul_FP(Y['G'], Y_pred['G']) + calcul_FP(Y['R'], Y_pred['R']) + calcul_FP(Y['H'], Y_pred['H']) + calcul_FP(Y['S'], Y_pred['S'])
    FN = calcul_FN(Y['G'], Y_pred['G']) + calcul_FN(Y['R'], Y_pred['R']) + calcul_FN(Y['H'], Y_pred['H']) + calcul_FN(Y['S'], Y_pred['S'])
    return {
        'TP': TP,
        'FP': FP,
        'FN': FN,
        'TN': TN,
    }


def     calcul_accuracy(Y, Y_pred):
    '''
    Calculate Accuracy of the Algorithm
    '''
    accuracy = ft_sum([int(y == y_pred) for y, y_pred in zip(Y, Y_pred)]) / len(Y)
    return accuracy


def     print_precision(Theta, X, labels):
    '''
    Print precision of the algorithm using different metrics:
    - precision-recall
    - F1 Score
    - Accuracy
    '''
    labels_pred = prediction(Theta, X)
    # Transform Ys to Dictionary of Ys
    Y = get_dict_Y(labels)
    Y_pred = get_dict_Y(labels_pred)
    ###################################
    # Confusion Matrix:
    CM = calcul_confusionDict(Y, Y_pred)
    # Precision / Recall:
    precision = CM['TP'] / (CM['TP'] + CM['FP'])
    recall = CM['TP'] / (CM['TP'] + CM['FN'])
    # F1 Score:
    F1 =  (2 * precision * recall) / (precision + recall)
    # Balanced Accuracy:
    balancedAccuracy = (recall + (CM['TN'] / (CM['TN'] + CM['FP']))) / 2
    # Accuracy:
    accuracy = calcul_accuracy(labels, labels_pred)
    print('\nPrecision of the algorithm:')
    print(f'Accuracy : {accuracy}')
    print('-----------------------------')
    print(CM)
    print('-----------------------------')
    print(f'Precision: {precision}')
    print(f'Recall   : {recall}')
    print(f'F1 score : {F1}')
    print(f'Balanced Accuracy: {F1}')
