# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/18 18:36:47 by obelouch          #+#    #+#              #
#    Updated: 2020/12/18 18:36:47 by obelouch         ###   ########.fr        #
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

from mylib.consts import bcolors, errors
from os import path
import pandas as pd
import sys


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
    print('python3 logreg_train.py <_train dataset path_>')
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


def     read_clean_csv(csvFile):
    '''
    Read the CSV & transform it to DataFrame 
    '''
    try:
        df = pd.read_csv(
                csvFile,
                # Columns to include
                usecols=[1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            )
    except:
        print('Can\'t transform the CSV into dataframe!')
        exit(1)
    return df


def     logreg_train():
    '''
    Train the logistic regression model with the dataset_train 
    '''
    # Check and get the CSV filename
    filename = get_filename()
    df = read_clean_csv(filename)
    X = df.iloc[:, 6:]
    Y = df['Hogwarts House']
    print('-------------------  X  ---------------------')
    print(X)
    print('-------------------  Y  ---------------------')
    print(Y)


# Launch the Logistic Regression training:
logreg_train()