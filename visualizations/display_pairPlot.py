# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display_pairPlot.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/25 12:41:15 by obelouch          #+#    #+#              #
#    Updated: 2020/12/17 06:28:40 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
from numpy import isnan


def     scatter_plot(ax, row, col):
    '''
    Put the scatter of $row and $col
    '''
    


def     display_pairPlot(df_houses):
    '''
    Display pair plot of the data frame
    '''
    # Init Figure
    figure = plt.figure(figsize=(18,13))
    # Add Padding between subplots
    figure.subplots_adjust(hspace=.4)
    # Set Window Title
    figure.canvas.set_window_title('Pair plot of the dataset')
    ax = []
    for row in list(df_houses['G'].columns)[1:]:
        i = 0
        ###
        for col in list(df_houses['G'].columns)[1:]:
            ############# One Plot ###################
            ax.append(figure.add_subplot(13,13,i + 1))
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
            ##########################################
            i+=1
    # Legend
    plt.legend(
        bbox_to_anchor=(1.5,1),
        loc='upper left',
        borderaxespad=0
    )
    # Show
    plt.show()
