# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/15 02:30:19 by obelouch          #+#    #+#              #
#    Updated: 2020/12/17 06:03:42 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from visualizations.display_scatter import display_scatter_2f
from visualizations.get_df_houses import get_df_houses
import mylib.math as myMath
import sys
import re


# Error Macros:
ERROR_ARGC = 1
ERROR_SYNTAX = 2
ERROR_FLAG_1 = 3
ERROR_FLAG_2 = 4
ERROR_EQU_FEATURES = 5
ERROR_OUT_FEATURES = 6

# Global Variables (Features used):
F1 = 2  #'Astronomy'
F2 = 4  #'Defense Against the Dark Arts'


def     exit_usage(error):
    if error == ERROR_ARGC:
        print('\nError: Wrong number of arguments!')
    if error == ERROR_SYNTAX:
        print('\nError: in Syntax!')
    if error == ERROR_FLAG_1:
        print('\nError: Syntax Error in the first flag!')
    if error == ERROR_FLAG_2:
        print('\nError: Syntax Error in the second flag!')
    if error == ERROR_EQU_FEATURES:
        print('\nError: The feature numbers are equal!')
    if error == ERROR_OUT_FEATURES:
        print('\nError: one of the feature numbers is out of range!')
    print('\nUsage: python3 scatter_plot.py [-f1{< n1 >}  -f2{< n2 >}]')
    print('    -f1: precise the first feature to use')
    print('    -f2: precise the second feature to use')
    print('    n1 and n2: index of the features')
    exit(1)


def     set_courses(f1, f2):
    '''
    Set the courses
    '''
    global  F1
    global  F2
    # Test if the features numbers are in range:
    if f1 > 13 or f2 > 13:
        exit_usage(ERROR_OUT_FEATURES)
    # Test if the features numbers are not identical:
    if (f1 == f2):
        exit_usage(ERROR_EQU_FEATURES)
    # Change default courses:
    F1 = f1
    F2 = f2


def     pick_features():
    '''
    Pick the features to scatter if the syntax is correct
    '''
    # Check if nbr of args > 2
    if len(sys.argv) != 3:
        exit_usage(ERROR_ARGC)
    #### Check Syntax of the
    # first flag
    if not re.match(r'^-f1\{[0-9]+\}$', sys.argv[1]):
        exit_usage(ERROR_FLAG_1)
    # second flag
    if not re.match(r'^-f2\{[0-9]+\}$', sys.argv[2]):
        exit_usage(ERROR_FLAG_2)
    ############################
    # Pick the features nbrs
    try:
        f1 = int(re.findall(r'[0-9]+', sys.argv[1])[1])
        f2 = int(re.findall(r'[0-9]+', sys.argv[2])[1])
    except:
        exit_usage(ERROR_SYNTAX)
    # Change default courses:
    set_courses(f1, f2)
    

def     scatter_plot():
    '''
    displays a scatter plot That show thee 2 features that are similar
    '''
    # Pick Features
    if len(sys.argv) > 1:
        pick_features()
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses('ressources/dataset_train.csv')
    # Display the Scatter of the 2 similar features
    display_scatter_2f(df_houses, F1, F2)


# Launch the program
scatter_plot()