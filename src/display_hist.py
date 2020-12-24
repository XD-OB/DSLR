# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display_hist.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/25 12:41:15 by obelouch          #+#    #+#              #
#    Updated: 2020/11/25 12:41:15 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
from numpy import isnan


def     display_histograms(df_houses):
    '''
    Display Histograms of the Houses
    '''
    # Init Figure
    figure = plt.figure(figsize=(13,9))
    # Add Padding between subplots
    figure.subplots_adjust(hspace=.5)
    # Set Window Title
    figure.canvas.set_window_title('Histogram of each course')
    ax = []
    i = 0
    ###
    for col in list(df_houses['G'].columns)[1:]:
        ax.append(figure.add_subplot(4,4,i + 1))
        ### Ravenclaw Histogram
        myarray = df_houses['R'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            alpha=0.4,
            bins='auto',
            color='#0000FF',
            label='Ravenclaw',
        )
        ### Hufflepuff Histogram
        myarray = df_houses['H'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            alpha=0.5,
            bins='auto',
            color='#CCCC00',
            label='Hufflepuff',
        )
        ### Gryffindor Histogram
        myarray = df_houses['G'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            alpha=0.4,
            bins='auto',
            color='#FF0000',
            label='Gryffindor',
        )
        ### Slytherin Histogram
        myarray = df_houses['S'].loc[:, col]
        myarray = myarray[~isnan(myarray)]
        ax[i].hist(
            myarray,
            alpha=0.4,
            bins='auto',
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


def     display_histogram(df_houses, f):
    '''
    Display the histogram of the course selected by the user, or by default
    the homogenous one (CMC)
    '''
    course = df_houses['G'].columns[f]
    # Init Figure
    figure = plt.figure(figsize=(10,8))
    # Set Window Title
    figure.canvas.set_window_title(f'Histogram of the course  "{course}"')
    ### Ravenclaw Histogram
    myarray = df_houses['R'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#0000FF',
        label='Ravenclaw',
    )
    ### Hufflepuff Histogram
    myarray = df_houses['H'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.5,
        bins='auto',
        color='#CCCC00',
        label='Hufflepuff',
    )
    ### Gryffindor Histogram
    myarray = df_houses['G'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#FF0000',
        label='Gryffindor',
    )
    ### Slytherin Histogram
    myarray = df_houses['S'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#00FF00',
        label='Slytherin',
    )
    ########
    plt.legend(loc='upper left')
    plt.ylabel('number of students')
    plt.xlabel('Marks')
    plt.title(course)
    # Adds major gridlines
    plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    # Show
    plt.show()
