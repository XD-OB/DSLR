# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 00:05:48 by obelouch          #+#    #+#              #
#    Updated: 2020/12/19 01:13:30 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.csvTools import get_df_from_csv
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
    print('python3 logreg_predict.py <_dataset_> <_weights file_>')
    exit(1)


def     check_csvFile(filename):
    '''
    Check if the filename is a valid CSV file
    '''
    if not path.exists(filename):
        exit_usage(errors.NOT_FILE)
    if not filename.endswith('.csv'):
        exit_usage(errors.NOT_CSV)


def     logreg_predict():
    '''
    Return a CSV of the predicted values using the:
    training dataset & a file that contain weights
    '''
    if len(sys.argv != 3):
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
        usecols=None
    )


# Launch the predict program
logreg_predict()