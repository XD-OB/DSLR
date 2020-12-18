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


from describes.print import exit_usage, print_describe
from mylib.math import ft_isNaN, ft_percentile
from describes.description import get_description
from mylib.consts import errors
from os import path
import pandas as pd
import sys


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


def     get_df_from_csv(csvFile):
    '''
    Read the CSV & transform it to DataFrame 
    '''
    try:
        df = pd.read_csv(
                csvFile,
                # Columns to include
                usecols=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            )
    except:
        print('Can\'t transform the CSV into dataframe!')
        exit(1)
    return df


def     describe():
    '''
    The Describe Program
    '''
    csvFile = get_filename()
    df = get_df_from_csv(csvFile)
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