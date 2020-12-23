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

# Global Variable:
dataset_file = 'ressources/dataset_train.csv'
is_all = False


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
    else:
        print('Syntax!')
    print(f'\n{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 histogram.py %s[-d]%s' % (bcolors.OKCYAN, bcolors.ENDC))
    print('       %s-d%s: Show all features histograms' % (bcolors.BOLD, bcolors.ENDC))
    exit(1)


def     set_flag(flags):
    '''
    Set the Global variable is_all
    '''
    global  is_all
    if len(flags) > 1:
        exit_usage(errors.FLAG_NBR)
    if flags[0] != 'd':
        exit_usage(errors.WRONG_FLAG)
    is_all = True


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
    # Display the Histogram of the homogenous course (Arithmancy)
    dh.display_arithmancy_histogram(df_houses)


# Launch the program
histogram()