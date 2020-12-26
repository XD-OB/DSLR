# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/18 18:36:47 by obelouch          #+#    #+#              #
#    Updated: 2020/12/26 16:50:02 by aelouarg         ###   ########.fr        #
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
from mylib.libft import get_flags_and_args
from src.algorithms import get_theta
from os import path
import numpy as np
import sys

# Global Variables:
algo = 'BGD'


def     print_loading():
    '''
    Print The Loading Message depend on the Algo type
    '''
    print(f'\nTraining using {bcolors.BOLD}', end='')
    if algo == 'SGD':
        print('Stochastic Gradient Descent', end='')
    else:
        print('Batch Gradient Descent', end='')
    print(f'{bcolors.ENDC} Algorithm ....\n')


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
    elif error == errors.FLAG_NBR:
        print('Too much options used!')
    elif error == errors.WRONG_FLAG:
        print('Wrong option used!')
    else:
        print('Can\'t read the file!')
    print(f'{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 logreg_train.py [-BGD | -SGD] <_train dataset_>')
    print('       -BGD: Batch Gradient Descent Algorithm')
    print('       -SGD: Stochastic Gradient Descent Algorithm')
    exit(1)


def     get_filename(args):
    '''
    Check & take the dataset file from the argument
    '''
    if len(args) > 1:
        exit_usage(errors.ARG_NBR)
    if len(args) == 0:
        exit_usage(errors.NO_ARG)
    filename = args[0]
    if not path.exists(filename):
        exit_usage(errors.NOT_FILE)
    if not filename.endswith('.csv'):
        exit_usage(errors.NOT_CSV)
    return filename


def     set_algorithm(flags):
    '''
    Set the Algorithm
    '''
    global  algo
    if len(flags) > 1:
        exit_usage(errors.FLAG_NBR)
    if len(flags) == 1:
        option = flags[0]
        if option not in ['BGD', 'SGD']:
            exit_usage(errors.WRONG_FLAG)
        algo = option

def     check_data(houses):
    '''
    Check House Data if empty
    '''
    for elt in houses: 
        if (elt == 0):
            print("%sError%s: Wrong Data" % (bcolors.FAIL, bcolors.ENDC))
            exit(1)


def     logreg_train():
    '''
    Train the logistic regression model with the dataset_train 
    '''
    # Get Arguments & Flags
    flags, args = get_flags_and_args()
    # Check & Set Algorithm:
    set_algorithm(flags)
    # Check & Get the CSV filename
    filename = get_filename(args)
    trainSet = get_df_from_csv(
        filename,
        [1, 8, 9, 10, 11, 12, 13, 17, 18]
    )
    # Test House Coulmn:
    check_data(trainSet.loc[:, "Hogwarts House"])
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
    # Get Theta depend on selected algorithm
    Theta = get_theta(X, Y, algo)
    # Print Weights in a file:
    Theta.to_csv(
        'weights.csv',
        index=False,
        sep=',',
    )
    # Print Precision:
    print(f'{bcolors.OKGREEN}Training DONE{bcolors.ENDC} ✅\n')
    print_precision(Theta, X, Y)


# Launch the Logistic Regression training:
logreg_train()
