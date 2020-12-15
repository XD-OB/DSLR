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

# Errors Numbers
ERROR_NO_ARG = -1
ERROR_ARG_NBR = -2
ERROR_NOT_CSV = -3
ERROR_NOT_FILE = -4

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
    elif (error == ERROR_NOT_FILE):
        print('Error: File not Found!')
    print('Usage: ./describe < CSV dataset >')
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