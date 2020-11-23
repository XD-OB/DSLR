# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/23 19:21:09 by obelouch          #+#    #+#              #
#    Updated: 2020/11/23 19:21:09 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from numpy import floor, ceil


def     ft_isNaN(nbr):
    '''
    test if the nbr is NAN
    '''
    return nbr != nbr

def     ft_percentile(ordList, i_th):
    '''
    Take a ordered List with the rank in percent then return the percentile  
    '''
    index = (i_th / 100) * (len(ordList) - 1)
    i_f = floor(index)
    i_c = ceil(index)

    if i_f == i_c:
        return ordList[int(index)]

    d0 = ordList[int(i_f)] * (i_c - index)
    d1 = ordList[int(i_c)] * (index - i_f)
    return d0 + d1