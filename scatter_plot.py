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

from src.display_scatter import display_scatter_2f
from src.df_houses import get_df_houses
from mylib.libft import get_flags_and_args
from mylib.consts import bcolors, errors
import mylib.math as myMath
import sys
import re


# Global Variables (Features used):
F1 = 2  #'Astronomy'
F2 = 4  #'Defense Against the Dark Arts'
dataset_file = 'ressources/dataset_train.csv'


def     exit_usage(error):
    '''
    Print the error Msg and Exit 
    '''
    print(f'\n{bcolors.FAIL}Error{bcolors.ENDC}: ', end='')
    if error == errors.ARG_NBR:
        print('Wrong number of arguments!')
    elif error == errors.FLAG_NBR:
        print('Wrong number of flags!')
    elif error == errors.SYNTAX:
        print('in Syntax!')
    elif error == errors.FLAG_1:
        print('Syntax Error in the first flag!')
    elif error == errors.FLAG_2:
        print('Syntax Error in the second flag!')
    elif error == errors.EQU_FTRS:
        print('The feature numbers are equal!')
    elif error == errors.OUT_FTRS:
        print('One of the feature numbers is out of range!')
    print(f'\n{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 scatter_plot.py %s[-f1{n1}  -f2{n2}]%s' % (bcolors.OKCYAN, bcolors.ENDC))
    print('    %s-f1%s: precise the first feature to use' % (bcolors.BOLD, bcolors.ENDC))
    print('    %s-f2%s: precise the second feature to use' % (bcolors.BOLD, bcolors.ENDC))
    print('    %sn1%s and %sn2%s: index of the features' % (bcolors.BOLD, bcolors.ENDC, bcolors.BOLD, bcolors.ENDC))
    exit(1)


def     set_courses(flags):
    '''
    Check & Set courses from flags
    '''
    global  F1
    global  F2

    if len(flags) != 2:
        exit_usage(errors.FLAG_NBR)
    #### Check Syntax of the flags ###############
    # first flag
    if not re.match(r'^f1\{[0-9]+\}$', flags[0]):
        exit_usage(errors.FLAG_1)
    # second flag
    if not re.match(r'^f2\{[0-9]+\}$', flags[1]):
        exit_usage(errors.FLAG_2)
    ##############################################
    # Pick the features nbrs
    try:
        f1 = int(re.findall(r'[0-9]+', flags[0])[1])
        f2 = int(re.findall(r'[0-9]+', flags[1])[1])
    except:
        exit_usage(errors.SYNTAX)
    # Test if the features numbers are in range:
    if f1 < 1 or f1 > 13 or f2 < 1 or f2 > 13:
        exit_usage(errors.OUT_FTRS)
    # Test if the features numbers are not identical:
    if f1 == f2:
        exit_usage(errors.EQU_FTRS)
    # Change default courses:
    F1 = f1
    F2 = f2


def     scatter_plot():
    '''
    displays a scatter plot That show thee 2 features that are similar
    '''
    # Get Arguments & Flags
    flags, args = get_flags_and_args()
    # Test if there is an addictional Args
    if len(args) > 0:
        exit_usage(errors.ARG_NBR)
    # Check & Set Courses from flags
    if len(flags) > 0:
        set_courses(flags)
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses(dataset_file)
    # Display the Scatter of the 2 similar features
    display_scatter_2f(df_houses, F1, F2)


# Launch the program
scatter_plot()