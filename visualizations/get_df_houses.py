# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_df_houses.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/15 02:45:03 by obelouch          #+#    #+#              #
#    Updated: 2020/12/15 02:45:03 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import pandas as pd
from os.path import isfile


def     read_corrFieldCsv(csvFile):
    '''
    Read the CSV & transform it to a grouped DataFrame 
    '''
    df = pd.read_csv(
            csvFile,
            # Columns to include
            usecols=[1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        )
    return df


def     get_df_houses(filename):
    '''
    Return a Dataframes dictionary of each house from a CSV file
    '''
    # Chack if the existance of the file:
    if not isfile(filename):
        print('ERROR: File not Found!')
        exit(1)
    # Read the data from the file
    df = read_corrFieldCsv(filename)
    # Dictionary contain a devide DataFrame for each House
    df_houses = {}
    df_houses['G'] = df[df['Hogwarts House'] == 'Gryffindor']
    df_houses['H'] = df[df['Hogwarts House'] == 'Hufflepuff']
    df_houses['S'] = df[df['Hogwarts House'] == 'Slytherin']
    df_houses['R'] = df[df['Hogwarts House'] == 'Ravenclaw']
    return df_houses
