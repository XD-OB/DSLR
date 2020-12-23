# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvTools.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 00:43:25 by obelouch          #+#    #+#              #
#    Updated: 2020/12/23 01:41:55 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from os import path

def     get_df_from_csv(csvFile, usecols=None):
    '''
    Read the CSV & return the dataframe with the selected features
    '''
    try:
        if usecols != None:
            df = pd.read_csv(
                    csvFile,
                    # Columns to include
                    usecols=usecols
                )
        else:
            df = pd.read_csv(csvFile)
    except:
        print('Can\'t transform the CSV into dataframe!')
        exit(1)
    # drop the rows that contain a NAN value
    df = df.dropna()
    return df


def     check_csvFile(filename):
    '''
    Check if the filename is a valid CSV file
    '''
    if not path.exists(filename):
        return 1
    if not filename.endswith('.csv'):
        return 2
    return 0
