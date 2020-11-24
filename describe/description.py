# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    description.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 17:08:53 by obelouch          #+#    #+#              #
#    Updated: 2020/11/24 17:08:53 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from describe.math import ft_percentile, ft_isNaN


def     calculate_mean_count(df, description, nbr_rows, nbr_cols):
    '''
    Calculate mean & count for the features and put it in the dictionary
    '''
    description['Count'] = [0] * nbr_cols
    description['Mean'] =  [0] * nbr_cols

    for col in range(nbr_cols):
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                description['Count'][col] += 1
                description['Mean'][col] += n
        description['Mean'][col] /= description['Count'][col]


def     calculate_std_percentiles(df, description, nbr_rows, nbr_cols):
    '''
    Calculate the Standard Deviation & percentiles for the features
    and put it in the dictionary
    '''
    description['Std'] = [0] * nbr_cols
    description['25%'] = [0] * nbr_cols
    description['50%'] = [0] * nbr_cols
    description['75%'] = [0] * nbr_cols

    for col in range(nbr_cols):
        count = description['Count'][col]
        mean = description['Mean'][col]
        ######## Calculate percentile #############
        order_col = sorted(filter(lambda n: not ft_isNaN(n), df.iloc[:, col]))
        description['25%'][col] = ft_percentile(order_col, 25)
        description['50%'][col] = ft_percentile(order_col, 50)
        description['75%'][col] = ft_percentile(order_col, 75)
        ###########################################
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                description['Std'][col] += (n - mean) ** 2
        description['Std'][col] = (description['Std'][col] / (count - 1)) ** 0.5


def     calculate_min_max(df, description, nbr_rows, nbr_cols):
    '''
    Calculate the Min & Max for the features and put it in the dictionary
    '''
    description['Min'] = [0] * nbr_cols
    description['Max'] = [0] * nbr_cols

    for col in range(nbr_cols):
        min = float('inf')
        max = float('-inf')
        for row in range(nbr_rows):
            n = df.iloc[row, col]
            if not ft_isNaN(n):
                if n < min:
                    min = n
                if n > max:
                    max = n
        description['Min'][col] = min
        description['Max'][col] = max


def     get_description(df):
    '''
    Fill the description dictionary with all the features
    '''
    # Description dictionary
    description = {}
    # For the shape:   0 = Rows  |  1 = Columns
    shape = df.shape
    description['Columns'] = df.columns.values
    calculate_mean_count(df, description, shape[0], shape[1])
    calculate_std_percentiles(df, description, shape[0], shape[1])
    calculate_min_max(df, description, shape[0], shape[1])
    return description