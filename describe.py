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

from describe.print import exit_usage, print_describe
from describe.math import ft_isNaN, ft_percentile
from describe.description import get_description
from os.path import isfile
from sys import argv
import pandas as pd
import describe.consts


def     read_clean_df(csvFile):
    '''
    Read the CSV & transform it to DataFrame 
    '''
    # Test file exist
    if not isfile(csvFile):
        exit_usage(ERROR_NOT_FILE)
    # Test format of the file === CSV
    if not '.csv' in csvFile:
        exit_usage(ERROR_NOT_CSV)
    df = pd.read_csv(
            csvFile,
            # Set Index 0 as Row name
            index_col = 0,
        )
    # Drop all none numerical columns
    df = df._get_numeric_data()
    return df


def     describe():
    '''
    The Describe Program
    '''
    if len(argv) == 1:
        exit_usage(ERROR_NO_ARG)
    if len(argv) > 2:
        exit_usage(ERROR_ARG_NBR)
    csvFile = argv[1]
    df = read_clean_df(csvFile)
    description = get_description(df)
    # print(df)
    # print('------ description  --------')
    # print(description)
    # print('------ sys describe --------')
    # print(df.describe())
    # print('------  description --------')
    print_describe(description)

# Launch the program
describe()