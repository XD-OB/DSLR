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

COURSE = 'Care of Magical Creatures'

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


def     display_arithmancy_histogram(df_houses):
    '''
    Display the histogram of the course that have homogeneous score
    distribution between all four houses
    '''
    # Init Figure
    figure = plt.figure(figsize=(10,8))
    # Set Window Title
    figure.canvas.set_window_title('Histogram of the course  " Care of Magical Creatures "')
    ### Ravenclaw Histogram
    myarray = df_houses['R'].loc[:, COURSE]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#0000FF',
        label='Ravenclaw',
    )
    ### Hufflepuff Histogram
    myarray = df_houses['H'].loc[:, COURSE]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.5,
        bins='auto',
        color='#CCCC00',
        label='Hufflepuff',
    )
    ### Gryffindor Histogram
    myarray = df_houses['G'].loc[:, COURSE]
    myarray = myarray[~isnan(myarray)]
    plt.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#FF0000',
        label='Gryffindor',
    )
    ### Slytherin Histogram
    myarray = df_houses['S'].loc[:, COURSE]
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
    plt.title(COURSE)
    # Adds major gridlines
    plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    # Show
    plt.show()
