# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 00:05:48 by obelouch          #+#    #+#              #
#    Updated: 2020/12/23 03:15:17 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.csvTools import get_df_from_csv, check_csvFile
from mylib.libft import get_flags_and_args
from mylib.consts import bcolors, errors
from src.standarize import standarize_X
from src.prediction import prediction
from mylib.math import ft_max
from os import path
import pandas as pd
import numpy as np
import sys

# Global Variables:
is_print = False


def     exit_usage(error, filename="file"):
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
    elif error == errors.WRONG_FLAG:
        print('Wrong option used!')
    else:
        print(f'Can\'t read the file {filename}!')
    print(f'{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 logreg_predict.py [-p] <_dataset_> <_weights file_>')
    print('       -p: Print the result with the students names in the stdout\n')
    exit(1)


def     show_result(predict_df):
    '''
    Show the result in a CSV file or in the terminal based on the flag
    '''
    if is_print == True:
        # Show the result
        ## Gryffindor:
        print(f'{bcolors.FAIL}------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Gryffindor'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.FAIL}--------- Gryffindor [{count}] ---------{bcolors.ENDC}\n')
        ## Hufflepuff:
        print(f'{bcolors.WARNING}-------------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Hufflepuff'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.WARNING}--------- Hufflepuff [{count}] ---------{bcolors.ENDC}\n')
        ## Ravenclaw
        print(f'{bcolors.OKBLUE}------------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Ravenclaw'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.OKBLUE}--------- Ravenclaw [{count}] ---------{bcolors.ENDC}\n')
        ## Slytherin
        print(f'{bcolors.OKGREEN}-----------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Slytherin'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.OKGREEN}---------- Slytherin [{count}] ---------{bcolors.ENDC}\n')
    else:
        try:
            # Write the result in a csv file:
            predict_df.to_csv(
                'houses.csv',
                index_label= 'Index',
                columns=['Hogwarts House']
            )
            # Print Finish message:
            print('\n%sSuccess:%s ' % (bcolors.OKGREEN, bcolors.ENDC) , end='')
            print('The prediction result is stored in %shouses.csv%s' % (bcolors.OKCYAN, bcolors.ENDC))
        except:
            print('\n%sFail:%s The prediction result is not stored!' % (bcolors.FAIL, bcolors.ENDC))


def     get_fileNames(args):
    '''
    Check & Get the files names from args
    '''
    if len(args) != 2:
        exit_usage(errors.ARG_NBR)
    # Check the CSV files
    check_csvFile(args[0])
    check_csvFile(args[1])
    return [
        args[0],
        args[1],
    ]


def     set_print(flags):
    '''
    Set 'is_print' Variable
    '''
    global  is_print
    if len(flags) > 1:
        exit_usage(errors.MUCH_FLAG)
    if len(flags) == 1:
        if flags[0] != 'p':
            exit_usage(errors.WRONG_FLAG)
        is_print = True


def     logreg_predict():
    '''
    Return a CSV of the predicted values using the:
    training dataset & a file that contain weights
    '''
    # Get Arguments & Flags
    flags, args = get_flags_and_args()
    # Check & Set Print:
    set_print(flags)
    # Check & Get the CSV filename
    fileName = get_fileNames(args)
    # take the dataframe from the files
    testSet = get_df_from_csv(
        fileName[0],
        [0, 2, 3, 8, 9, 10, 11, 12, 13, 17, 18]
    )
    weights = get_df_from_csv(
        fileName[1],
    )
    # Check Dimensions of the weights file
    if weights.shape != (9, 4):
        exit_usage(errors.WEIGHTS_DIM)
    # Build X Matrice
    # (remove the index column and add X0 column full of 1):
    X = np.concatenate(
        (
            np.ones((testSet.shape[0], 1)),
            standarize_X(testSet.iloc[:, 3:]),
        ),
        # concat in columns
        axis=1
    )
    # Predict DF:
    predict_dict = {
        'Hogwarts House': prediction(weights, X),
        'First Name': testSet.loc[:, 'First Name'],
        'Last Name': testSet.loc[:, 'Last Name'],
    }
    predict_df = pd.DataFrame(
        predict_dict,
        index=list(testSet['Index']),
    )
    # Show the result
    show_result(predict_df)


# Launch the predict program
logreg_predict()