# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/18 18:36:47 by obelouch          #+#    #+#              #
#    Updated: 2020/12/19 00:50:31 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

########### Choice of features #################################################
#                                                                              #
# Some features are homogenous or coherant with other ones, so there           #
#  existance is not necessary for training the model and can give use          #
#  a complex hypothesis that will cause 'Overfitting'                          #
# Our choice was to remove:                                                    #
#  - Arithmancy               :  Homogenous                                    #
#  - Astronomy                :  Similar to 'Defense Against the Dark Arts'    #
#  - Transfiguration          :  Semi similar to 'History of Magic'            #
#  - Potions                  :  Semi homogenous                               #
#  - Care of Magical Creatures:  Semi homogenous                               #
#                                                                              #
################################################################################

from src.standarize import standarize_X
from src.precision import print_precision
from mylib.csvTools import get_df_from_csv
from mylib.consts import bcolors, errors
from mylib.math import sigmoid
from os import path
import pandas as pd
import numpy as np
import sys

# Max Iteration Macro:
MAX_ITER = 1000

# Global Variables:
algo = 'BGD'


def     print_loading():
    '''
    Print The Loading Message depend on the Algo type
    '''
    print('\nTraining using ', end='')
    if algo == 'SGD':
        print('Stochastic Gradient Descent Algorithm ....\n')
    elif algo == 'LS':
        print('Least Squares Algorithm ....\n')
    else:
        print('Batch Gradient Descent Algorithm ....\n')


def     exit_usage(error):
    '''
    Print the error Msg and Exit 
    '''
    print(f'\n{bcolors.FAIL}Error{bcolors.ENDC}: ', end='')
    if error == errors.ARG_NBR:
        print('Wrong number of arguments!')
    elif error == errors.NO_ARG:
        print('No file is provided!')
    elif error == errors.NOT_FILE:
        print('File not found!')
    elif error == errors.NOT_CSV:
        print('Wrong file extension, accept only CSV!')
    else:
        print('Can\'t read the file!')
    print(f'{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 logreg_train.py <_train dataset_>')
    exit(1)


def     get_filename():
    '''
    Take and check the dataset file from the argument
    '''
    if len(sys.argv) > 2:
        exit_usage(errors.ARG_NBR)
    if len(sys.argv) == 1:
        exit_usage(errors.NO_ARG)
    filename = sys.argv[1]
    if not path.exists(filename):
        exit_usage(errors.NOT_FILE)
    if not filename.endswith('.csv'):
        exit_usage(errors.NOT_CSV)
    return filename


def     get_Y(labels, house):
    '''
    Create the One vs All Ys
    '''
    Y = np.array([int(y == house) for y in labels], ndmin=2)
    return np.transpose(Y)


def     gradient_descent(X, Y):
    '''
    Apply The Gradient descent 
    '''
    # Learning Rate
    alpha = 0.1
    # Init Theta
    theta = np.zeros((9,1))
    # Launch the Gradient Algorithm
    for _ in range(MAX_ITER):
        theta -= (alpha / Y.shape[0]) * np.transpose(X).dot(sigmoid(X.dot(theta)) - Y)
    # Rehape theta to a simple vector before return it
    theta = np.reshape(theta, (9,))
    return theta


def     logreg_train():
    '''
    Train the logistic regression model with the dataset_train 
    '''
    # Check and get the CSV filename
    filename = get_filename()
    trainSet = get_df_from_csv(
        filename,
        [1, 8, 9, 10, 11, 12, 13, 17, 18]
    )
    # Print Loading:
    print_loading()
    # The X (features) Matrice [m x 9]
    # (remove the index column and add X0 column full of 1):
    X = np.concatenate(
        (
            np.ones((trainSet.shape[0], 1)),
            standarize_X(trainSet.iloc[:, 1:]),
        ),
        # concat in columns
        axis=1
    )
    # The Y (labels) Vector [m x 1]
    Y = trainSet['Hogwarts House']
    # Get Theta from Gradient Descent:
    result_dict = {
        'G': gradient_descent(X, get_Y(Y, 'Gryffindor')),
        'R': gradient_descent(X, get_Y(Y, 'Ravenclaw')),
        'H': gradient_descent(X, get_Y(Y, 'Hufflepuff')),
        'S': gradient_descent(X, get_Y(Y, 'Slytherin')),
    }
    Theta = pd.DataFrame(result_dict)
    # Print Weights in a file:
    Theta.to_csv(
        'weights.csv',
        index=False,
        sep='\t',
    )
    # Print Precision:
    print('Training DONE ✅\n')
    print_precision(Theta, X, Y)


# Launch the Logistic Regression training:
logreg_train()