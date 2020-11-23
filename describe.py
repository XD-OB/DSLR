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

from describe.math import ft_isNaN, ft_percentile
from sys import argv
import pandas as pd

# Errors Numbers
ERROR_NO_ARG = -1
ERROR_ARG_NBR = -2
ERROR_NOT_CSV = -3

# Description dictionary
description = {}


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


def     calculate_std_percentiles(df, nbr_rows, nbr_cols):
    '''
    Calculate the Standard Deviation & percentiles for the features
    and put it in the dictionary
    '''
    global  description

    description['Std'] = [0] * nbr_cols
    description['25%'] = [0] * nbr_cols
    description['50%'] = [0] * nbr_cols
    description['75%'] = [0] * nbr_cols

    for col in range(nbr_cols):
        count = description['Count'][col]
        mean = description['Mean'][col]
        ######## Calculate percentile #############
        order_col = sorted(filter(lambda n: not ft_isNaN(n), df.iloc[:, col]))
        description['25%'][col] = ft_percentile(order_col, 25)
        description['50%'][col] = ft_percentile(order_col, 50)
        description['75%'][col] = ft_percentile(order_col, 75)
        ###########################################
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                description['Std'][col] += (n - mean) ** 2
        description['Std'][col] = (description['Std'][col] / (count - 1)) ** 0.5


def     calculate_min_max(df, nbr_rows, nbr_cols):
    '''
    Calculate the Min & Max for the features and put it in the dictionary
    '''
    global  description

    description['Min'] = [0] * nbr_cols
    description['Max'] = [0] * nbr_cols

    for col in range(nbr_cols):
        min = float('inf')
        max = float('-inf')
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
    description['Columns'] = df.columns.values
    calculate_mean_count(df, shape[0], shape[1])
    calculate_std_percentiles(df, shape[0], shape[1])
    calculate_min_max(df, shape[0], shape[1])

def     print_describe():
    '''
    Print the description dictionary in the describe format
    '''
    # print columns names
    print('%7s' % '', end='')
    for i in range(len(description['Columns'])):
        print('%15s\t' % ('Feature ' + str(i + 1)), end='')
    # Print the Count Row
    print('\n%-7s' % 'Count', end='')
    for count in description['Count']:
        print('%15.6f\t' % count, end='')
    # Print the Mean Row
    print('\n%-7s' % 'Mean', end='')
    for mean in description['Mean']:
        print('%15.6f\t' % mean, end='')
    # Print the Standard variation Row
    print('\n%-7s' % 'Std', end='')
    for std in description['Std']:
        print('%15.6f\t' % std, end='')
    # Print the Minimum Row
    print('\n%-7s' % 'Min', end='')
    for min in description['Min']:
        print('%15.6f\t' % min, end='')
    # Print the 25th percentile Row
    print('\n%-7s' % '25%', end='')
    for th_25 in description['25%']:
        print('%15.6f\t' % th_25, end='')
    # Print the 50th percentile Row
    print('\n%-7s' % '50%', end='')
    for th_50 in description['50%']:
        print('%15.6f\t' % th_50, end='')
    # Print the 75th percentile Row
    print('\n%-7s' % '75%', end='')
    for th_75 in description['75%']:
        print('%15.6f\t' % th_75, end='')
    # Print the Maximum Row
    print('\n%-7s' % 'Max', end='')
    for max in description['Max']:
        print('%15.6f\t' % max, end='')
    print('')

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
    print('------ description  --------')
    print(description)
    print('------ sys describe --------')
    print(df.describe())
    print('------  description --------')
    print_describe()

describe()