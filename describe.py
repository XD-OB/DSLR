# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/23 09:41:24 by obelouch          #+#    #+#              #
#    Updated: 2020/11/23 14:10:03 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from sys import argv
import pandas as pd

# Errors Numbers
ERROR_NO_ARG = -1
ERROR_ARG_NBR = -2
ERROR_NOT_CSV = -3

# Description dictionary
description = {}

def     ft_isNaN(nbr):
    return nbr != nbr

def     exit_usage(error):
    '''
    Print the Usage & the Error Msg then Exit
    '''
    if (error == ERROR_NO_ARG):
        print('Error: No argument!')
    elif (error == ERROR_ARG_NBR):
        print('Error: Wrong number of arguments!')
    elif (error == ERROR_NOT_CSV):
        print('Error: Wrong format of the file!')
    print('Usage: ./describe < CSV dataset >')
    exit(1)

def     calculate_mean_count(df, nbr_rows, nbr_cols):
    '''
    Calculate mean & count for the features and put it in the dictionary
    '''
    global  description

    description['Count'] = [0] * nbr_cols
    description['Mean'] =  [0] * nbr_cols

    for col in range(nbr_cols):
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                description['Count'][col] += 1
                description['Mean'][col] += n
        description['Mean'][col] /= description['Count'][col]


def     calculate_std(df, nbr_rows, nbr_cols):
    '''
    Calculate the Standard Deviation for the features and put it in the dictionary
    '''
    global  description

    description['Std'] = [0] * nbr_cols

    for col in range(nbr_cols):
        count = description['Count'][col]
        mean = description['Mean'][col]
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                description['Std'][col] += (n - mean) ** 2
        description['Std'][col] = (description['Std'][col] / count) ** 0.5


def     calculate_percentiles(df, nbr_rows, nbr_cols):
    '''
    Calculate the Min & Max for the features and put it in the dictionary
    '''
    global  description

    description['25%'] = [0] * nbr_cols
    description['50%'] = [0] * nbr_cols
    description['75%'] = [0] * nbr_cols

    for col in range(nbr_cols):
        min = float('-inf')
        max = float('inf')
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                if n < min:
                    min = n
                if n > max:
                    max = n
        description['Min'][col] = min
        description['Max'][col] = max


def     calculate_min_max(df, nbr_rows, nbr_cols):
    '''
    Calculate the Min & Max for the features and put it in the dictionary
    '''
    global  description

    description['Min'] = [0] * nbr_cols
    description['Max'] = [0] * nbr_cols

    for col in range(nbr_cols):
        min = float('-inf')
        max = float('inf')
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                if n < min:
                    min = n
                if n > max:
                    max = n
        description['Min'][col] = min
        description['Max'][col] = max


def     read_clean_df(csvFile):
    '''
    Read the CSV & transform it to DataFrame 
    '''
    df = pd.read_csv(
            csvFile,
            # Set Index 0 as Row name
            index_col = 0,
        )
    # Drop all none numerical columns
    df = df._get_numeric_data()
    return df


def     fill_description(df):
    '''
    Fill the description dictionary with all the features
    '''
    # For the shape:   0 = Rows  |  1 = Columns
    shape = df.shape
    calculate_mean_count(df, shape[0], shape[1])
    calculate_std(df, shape[0], shape[1])
    calculate_min_max(df, shape[0], shape[1])
    calculate_percentiles(df, shape[0], shape[1])


def     describe():
    '''
    The Describe Program
    '''
    if (len(argv) == 1):
        exit_usage(ERROR_NO_ARG)
    if (len(argv) > 2):
        exit_usage(ERROR_ARG_NBR)
    csvFile = argv[1]
    if (not '.csv' in csvFile):
        exit_usage(ERROR_NOT_CSV)
    df = read_clean_df(csvFile)
    fill_description(df)
    print(df)
    print('-------------------------------------------')
    print(description['Count'])

describe()