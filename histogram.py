# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 17:31:50 by obelouch          #+#    #+#              #
#    Updated: 2020/11/24 17:31:50 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import matplotlib.pyplot as plt
from pandas import read_csv
from os.path import isfile
from numpy import isnan


FILE_NAME = 'ressources/dataset_train.csv'

def     read_df(csvFile):
    '''
    Read the CSV & transform it to a grouped DataFrame 
    '''
    df = read_csv(
            csvFile,
            # Columns to include
            usecols=[1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        )
    return df

def     display_histograms(df):
    '''
    Display the histograms of the Houses
    '''
    # Devide DataFrame for each house
    df_gryffindor = df[df['Hogwarts House'] == 'Gryffindor']
    df_hufflepuff = df[df['Hogwarts House'] == 'Hufflepuff']
    df_slytherin = df[df['Hogwarts House'] == 'Slytherin']
    df_ravenclaw = df[df['Hogwarts House'] == 'Ravenclaw']
    # Init Figure
    figure = plt.figure(figsize=(12,8))
    ax = []
    i = 0
    ###
    for col in df.columns:
        if col == 'Hogwarts House':
            continue
        ax.append(figure.add_subplot(4,4,i + 1))
        ### Ravenclaw Histogram
        myarray = df_ravenclaw.loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.4,
            color='#0000FF',
            label='Ravenclaw',
        )
        ### Hufflepuff Histogram
        myarray = df_hufflepuff.loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.5,
            color='#CCCC00',
            label='Hufflepuff',
        )
        ### Gryffindor Histogram
        myarray = df_gryffindor.loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.4,
            color='#FF0000',
            label='Gryffindor',
        )
        ### Slytherin Histogram
        myarray = df_slytherin.loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.4,
            color='#00FF00',
            label='Slytherin',
        )
        ######
        i+=1
    # Legend
    plt.legend(
        bbox_to_anchor=(1.5,1),
        loc='upper left',
        borderaxespad=0
    )
    # Show
    plt.show()
        


def     histogram():
    '''
    Display the Hogwarts course that has a homogeneous score
    distribution between all the four houses
    '''
    # Chack if the existance of the file:
    if not isfile(FILE_NAME):
        print('ERROR: File not Found!')
        exit(1)
    # Read the data from the file
    df = read_df('ressources/dataset_train.csv')
    display_histograms(df)


# Launch the program
histogram()