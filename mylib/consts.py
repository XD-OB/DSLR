# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    consts.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/18 20:09:04 by obelouch          #+#    #+#              #
#    Updated: 2020/12/19 04:11:34 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class   bcolors:
    '''
    Colors for print
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class   errors:
    '''
    Errors Macros
    '''
    # Errors Macros
    NO_ARG = 1
    SYNTAX = 2
    FLAG_1 = 3
    FLAG_2 = 4
    ARG_NBR = 5
    NOT_CSV = 6
    FLAG_NBR = 7
    EQU_FTRS = 8
    OUT_FTRS = 9
    NOT_FILE = 10
    WRONG_FLAG = 11
    WEIGHTS_DIM = 12