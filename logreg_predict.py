# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 00:05:48 by obelouch          #+#    #+#              #
#    Updated: 2020/12/19 05:58:54 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.csvTools import get_df_from_csv
from mylib.consts import bcolors, errors
from mylib.math import sigmoid, ft_max
from os import path
import pandas as pd
import numpy as np
import sys


# Houses Names:
houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']


def     h(Theta, X):
    '''
    Hypothesis finction
    '''
    return sigmoid(X.dot(Theta))


def     prediction(weights, X):
    '''
    Return a vector of Predicted Houses
    '''
    # Prediction Matrice:
    predict_matrice = h(weights, X)
    # Get the max column index of each row
    prediction = []
    for i in range(X.shape[0]):
        prediction.append(
            np.argmax(predict_matrice[i])
        )
    return prediction


def     exit_usage(filename, error):
    '''
    Print the error Msg and Exit 
    '''
    print(f'\n{bcolors.FAIL}Error{bcolors.ENDC}: ', end='')
    if error == errors.ARG_NBR:
        print('Wrong number of arguments!')
    elif error == errors.NO_ARG:
        print('No files is provided!')
    elif error == errors.NOT_FILE:
        print(f'File "{filename}" not found!')
    elif error == errors.NOT_CSV:
        print(f'Wrong extension of the file "{filename}", accept only CSV!')
    elif error == errors.WEIGHTS_DIM:
        print(f'Wrong Weights file content shape!')
    else:
        print(f'Can\'t read the file {filename}!')
    print(f'{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 logreg_predict.py <_dataset_> <_weights file_>')
    exit(1)


def     check_csvFile(filename):
    '''
    Check if the filename is a valid CSV file
    '''
    if not path.exists(filename):
        exit_usage(filename, errors.NOT_FILE)
    if not filename.endswith('.csv'):
        exit_usage(filename, errors.NOT_CSV)


def     logreg_predict():
    '''
    Return a CSV of the predicted values using the:
    training dataset & a file that contain weights
    '''
    if len(sys.argv) != 3:
        exit_usage(errors.ARG_NBR)
    file1_name = sys.argv[1]
    file2_name = sys.argv[2]
    # Check the CSV files
    check_csvFile(file1_name)
    check_csvFile(file2_name)
    # take the dataframe from the files
    testSet = get_df_from_csv(
        file1_name,
        [0, 8, 9, 10, 11, 12, 13, 17, 18]
    )
    weights = get_df_from_csv(
        file2_name,
    )
    # Check Dimensions of the weights file
    if weights.shape[0] != 9 or weights.shape[1] != 4:
        exit_usage(errors.WEITGHS_SHAPE)
    # Build X Matrice
    # (remove the index column and add X0 column full of 1):
    X = np.concatenate(
        (
            np.ones((testSet.shape[0], 1)),
            np.array(testSet.iloc[:, 1:]),
        ),
        # concat in columns
        axis=1
    )
    # Predict Houses:
    predict_houses = prediction(weights, X)
    print(predict_houses)


# Launch the predict program
logreg_predict()