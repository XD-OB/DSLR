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
import sys


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

def     display_histograms(df_houses):
    '''
    Display the histograms of the Houses
    '''
    # Init Figure
    figure = plt.figure(figsize=(13,9))
    # Add Padding between subplots
    figure.subplots_adjust(hspace=.5)
    ax = []
    i = 0
    ###
    for col in df_houses['G'].columns:
        if col == 'Hogwarts House':
            continue
        ax.append(figure.add_subplot(4,4,i + 1))
        ### Ravenclaw Histogram
        myarray = df_houses['R'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.4,
            color='#0000FF',
            label='Ravenclaw',
        )
        ### Hufflepuff Histogram
        myarray = df_houses['H'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.5,
            color='#CCCC00',
            label='Hufflepuff',
        )
        ### Gryffindor Histogram
        myarray = df_houses['G'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.4,
            color='#FF0000',
            label='Gryffindor',
        )
        ### Slytherin Histogram
        myarray = df_houses['S'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            bins=20,
            alpha=0.4,
            color='#00FF00',
            label='Slytherin',
        )
        ######
        ax[i].set_title(col)
        i+=1
    plt.legend(
        bbox_to_anchor=(1.5,1),
        loc='upper left',
        borderaxespad=0
    )
    # Show
    plt.show()


def     display_course_histogram(df_houses, course):
    '''
    Display the histograms of the Houses
    '''
    ### Ravenclaw Histogram
    myarray = df_houses['R'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        bins=20,
        alpha=0.4,
        color='#0000FF',
        label='Ravenclaw',
    )
    ### Hufflepuff Histogram
    myarray = df_houses['H'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        bins=20,
        alpha=0.5,
        color='#CCCC00',
        label='Hufflepuff',
    )
    ### Gryffindor Histogram
    myarray = df_houses['G'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        bins=20,
        alpha=0.4,
        color='#FF0000',
        label='Gryffindor',
    )
    ### Slytherin Histogram
    myarray = df_houses['S'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        bins=20,
        alpha=0.4,
        color='#00FF00',
        label='Slytherin',
    )
    ########
    plt.legend(loc='upper left')
    plt.ylabel('number of students')
    plt.xlabel('Marks')
    plt.title(course)
    # Show
    plt.show()


def     ft_mean(myarray):
    '''
    Mean of an array
    '''
    mean = 0
    for element in myarray:
        mean += element
    mean /= len(myarray)
    return mean

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


def     find_course(df_houses):
    '''
    Find the homogenous Course
    '''
    columns = df_houses['G'].columns
    scores = {}
    for col in columns:
        if col == 'Hogwarts House':
            continue
        means = {}
        means['G'] = ft_mean(df_houses['G'][col])
        means['H'] = ft_mean(df_houses['H'][col])
        means['S'] = ft_mean(df_houses['S'][col])
        means['R'] = ft_mean(df_houses['R'][col])
        scores[col] = ft_abs(ft_abs(means['G'] - means['H']) - ft_abs(means['S'] - means['R']))
    return dict_minValue_key(scores)


def     is_show_all():
    '''
    Test if the detail flag is present
    '''
    if len(sys.argv) != 2:
        return False
    if sys.argv[1] == '-d' or sys.argv[1] == '--details':
        return True
    return False


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
    # Dictionary contain a devide DataFrame for each House
    df_houses = {}
    df_houses['G'] = df[df['Hogwarts House'] == 'Gryffindor']
    df_houses['H'] = df[df['Hogwarts House'] == 'Hufflepuff']
    df_houses['S'] = df[df['Hogwarts House'] == 'Slytherin']
    df_houses['R'] = df[df['Hogwarts House'] == 'Ravenclaw']
    # Show all option
    if is_show_all():
        display_histograms(df_houses)
    # find the column that have homogenous score
    course = find_course(df_houses)
    # Display the Histogram of the homogenous course
    display_course_histogram(df_houses, course)


# Launch the program
histogram()