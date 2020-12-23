# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/23 09:41:24 by obelouch          #+#    #+#              #
#    Updated: 2020/12/18 23:57:33 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from src.description import get_description, print_describe
from mylib.csvTools import get_df_from_csv
from mylib.consts import bcolors, errors
from os import path
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
    print('python3 describe.py <_dataset.csv_>')
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
    if not path.isfile(filename):
        exit_usage(errors.NOT_FILE)
    if not filename.endswith('.csv'):
        exit_usage(errors.NOT_CSV)
    return filename


def     describe():
    '''
    The Describe Program
    '''
    csvFile = get_filename()
    df = get_df_from_csv(
        csvFile,
        usecols=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    )
    description = get_description(df)
    print_describe(description)


# Launch the program
describe()