# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 17:31:50 by obelouch          #+#    #+#              #
#    Updated: 2020/12/17 06:12:37 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from mylib.libft import get_flags_and_args
from src.df_houses import get_df_houses
from mylib.consts import bcolors, errors
import src.display_hist as dh
import re

# Global Variable:
dataset_file = 'ressources/dataset_train.csv'
is_all = False
feature = 11


def     exit_usage(error):
    '''
    Print the error Msg and Exit 
    '''
    print(f'\n{bcolors.FAIL}Error{bcolors.ENDC}: ', end='')
    if error == errors.ARG_NBR:
        print('Wrong number of arguments!')
    elif error == errors.FLAG_NBR:
        print('Too much options used!')
    elif error == errors.WRONG_FLAG:
        print('Wrong option used!')
    elif error == errors.OUT_FTRS:
        print('The feature numbers is out of range!')
    else:
        print('Syntax!')
    print(f'\n{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 histogram.py %s[-d | -f{n}]%s' % (bcolors.OKCYAN, bcolors.ENDC))
    print('       %s-d%s: Show all features histograms' % (bcolors.BOLD, bcolors.ENDC))
    print('       %s-f%s: Show histogram of the feature "n"' % (bcolors.BOLD, bcolors.ENDC))
    exit(1)


def     set_flag(flags):
    '''
    Set the Global variable is_all
    '''
    global  is_all
    global  feature

    if len(flags) > 1:
        exit_usage(errors.FLAG_NBR)
    if flags[0] == 'd':
        is_all = True
    elif re.match(r'^f\{[0-9]+\}$', flags[0]):
        try:
            tmp = int(re.findall(r'[0-9]+', flags[0])[0])
        except:
            exit_usage(errors.SYNTAX)
        if tmp < 1 or tmp > 13 :
            exit_usage(errors.OUT_FTRS)
        feature = tmp
    else:
        exit_usage(errors.WRONG_FLAG)


def     histogram():
    '''
    Display the Hogwarts course that has a homogeneous score
    distribution between all the four houses
    '''
    # Get Arguments & Flags
    flags, args = get_flags_and_args()
    # Check Arguments:
    if len(args) > 0:
        exit_usage(errors.ARG_NBR)
    if len(flags) > 0:
        set_flag(flags)
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses(dataset_file)
    # Show all histograms
    if is_all:
        dh.display_histograms(df_houses)
    # Default display the Histogram of the homogenous course (CMC)
    # or the selected course via -f
    else:
        dh.display_histogram(df_houses, feature)


# Launch the program
histogram()