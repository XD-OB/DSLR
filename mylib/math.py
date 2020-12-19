# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/25 12:26:44 by obelouch          #+#    #+#              #
#    Updated: 2020/12/19 04:21:20 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def     sigmoid(z):
    '''
    Sigmoid fonction
    '''
    return 1 / (1 + np.exp(z))


def     ft_isNaN(nbr):
    '''
    test if the nbr is NAN
    '''
    return nbr != nbr


def     ft_isnan(myarray):
    '''
    return a logical array of test NAN
    '''
    len_array = len(myarray)
    result = [False] * len_array
    for i in range(len_array):
        if myarray[i] != myarray[i]:
            result[i] = True
    return result


def     ft_percentile(ordList, i_th):
    '''
    Take a ordered List with the rank in percent then return the percentile  
    '''
    index = (i_th / 100) * (len(ordList) - 1)
    i_f = np.floor(index)
    i_c = np.ceil(index)

    if i_f == i_c:
        return ordList[int(index)]

    d0 = ordList[int(i_f)] * (i_c - index)
    d1 = ordList[int(i_c)] * (index - i_f)
    return d0 + d1


def     ft_standardized(myList):
    '''
    Standarize a list of data
    '''
    # Remove the NAN values
    myList = myList[~np.isnan(myList)]
    ###
    mean = ft_mean(myList)
    std = ft_std(myList)
    Z = []
    for value in myList:
        Z.append((value - mean) / std)
    return Z


def     ft_mean(myarray):
    '''
    Mean of an array
    '''
    mean = 0
    for element in myarray:
        mean += element
    mean /= len(myarray)
    return mean


def     ft_count(myarray):
    '''
    Count none NAN elements of an array
    '''
    len_array = 0
    for element in myarray:
        if element == element:
            len_array += 1
    return len_array


def     ft_min(myarray):
    '''
    Count none NAN elements of an array
    '''
    min = myarray[0]
    for element in myarray:
        if element < min:
            min = element
    return min


def     ft_max(myarray):
    '''
    Count none NAN elements of an array
    '''
    max = myarray[0]
    for element in myarray:
        if element > max:
            max = element
    return min


def     ft_std(myarray):
    '''
    Standard deviation of an array
    '''
    std = 0
    mean = ft_mean(myarray)
    for element in myarray:
        if not ft_isNaN(element):
            std += (element - mean) ** 2
    std = (std / (ft_count(myarray) - 1)) ** 0.5
    return  std


def     ft_abs(nbr):
    '''
    Absolute Value
    '''
    if nbr < 0:
        return -nbr
    return nbr 


def     dict_minValue_key(mydict):
    '''
    Return the key of the min value in a dictionary
    '''
    min_key = list(mydict.keys())[0]
    for key, value in mydict.items():
        if value < mydict[min_key]:
            min_key = key
    return min_key
