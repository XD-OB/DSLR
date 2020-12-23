# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/23 19:30:20 by marvin            #+#    #+#              #
#    Updated: 2020/11/23 19:30:20 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.consts import bcolors, errors


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
    print('python3 describe.py < csv_dataset >')
    exit(1)


def     print_describe(description):
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