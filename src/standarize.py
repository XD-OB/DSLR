# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    standarize.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 08:05:08 by obelouch          #+#    #+#              #
#    Updated: 2020/12/19 08:05:08 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.math import ft_standardized
import numpy as np

def     standarize_X(df_matrice):
    '''
    Standarize the matrice by standarize each column
    '''
    std_matrice = []
    for col in df_matrice.columns:
        std_matrice.append(
            ft_standardized(df_matrice[col])
        )
    return np.array(
        np.transpose(std_matrice)
    )