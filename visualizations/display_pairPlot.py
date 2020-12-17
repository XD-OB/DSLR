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

from visualizations.display_scatter import get_house_courses
import matplotlib.pyplot as plt
from numpy import isnan


def     histogram_plot(df_houses, figure, course, i):
    '''
    Put the Histogram of $row === $col
    '''
    ############# One Plot ###################
    new_ax = figure.add_subplot(13, 13, i)
    ### Ravenclaw Histogram
    myarray = df_houses['R'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    new_ax.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#0000FF',
        label='Ravenclaw',
    )
    ### Hufflepuff Histogram
    myarray = df_houses['H'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    new_ax.hist(
        myarray,
        alpha=0.5,
        bins='auto',
        color='#CCCC00',
        label='Hufflepuff',
    )
    ### Gryffindor Histogram
    myarray = df_houses['G'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    new_ax.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#FF0000',
        label='Gryffindor',
    )
    ### Slytherin Histogram
    myarray = df_houses['S'].loc[:, course]
    myarray = myarray[~isnan(myarray)]
    new_ax.hist(
        myarray,
        alpha=0.4,
        bins='auto',
        color='#00FF00',
        label='Slytherin',
    )
    ######
    #new_ax.set_title(course)
    ##########################################
    return new_ax


def     scatter_plot(df_houses, figure, row, col, i):
    '''
    Put the Scatter of $row and $col
    '''
    ############# One Plot ###################
    new_ax = figure.add_subplot(13, 13, i)
    ### Ravenclaw Histogram
    courses = get_house_courses(df_houses, 'R', row, col)
    new_ax.scatter(
        courses[row],
        courses[col],
        alpha=0.4,
        color='#0000FF',
        label='Ravenclaw',
    )
    ### Hufflepuff Histogram
    courses = get_house_courses(df_houses, 'H', row, col)
    new_ax.scatter(
        courses[row],
        courses[col],
        alpha=0.5,
        color='#CCCC00',
        label='Hufflepuff',
    )
    ### Gryffindor Histogram
    courses = get_house_courses(df_houses, 'G', row, col)
    new_ax.scatter(
        courses[row],
        courses[col],
        alpha=0.4,
        color='#FF0000',
        label='Gryffindor',
    )
    ### Slytherin Histogram
    courses = get_house_courses(df_houses, 'S', row, col)
    new_ax.scatter(
        courses[row],
        courses[col],
        alpha=0.4,
        color='#00FF00',
        label='Slytherin',
    )
    ######
    #new_ax.set_title(col)
    ##########################################
    return new_ax


def     display_pairPlot(df_houses):
    '''
    Display pair plot of the data frame
    '''
    # Init Figure
    figure = plt.figure(figsize=(40,30))
    # Add Padding between subplots
    figure.subplots_adjust(hspace=2)
    # Set Window Title
    figure.canvas.set_window_title('Pair plot of the dataset')
    ax = []
    i = 1
    for row in list(df_houses['G'].columns)[1:]:
        for col in list(df_houses['G'].columns)[1:]:
            ## Show Histograms in diagonal
            if row == col:
                # Histogram Plot:
                ax.append(
                    histogram_plot(
                        df_houses,
                        figure,
                        col,
                        i,
                    )
                )
            ###############################
            else:
                # Scatter Plot:
                ax.append(
                    scatter_plot(
                        df_houses,
                        figure,
                        row,
                        col,
                        i,
                    )
                )
            i += 1
    # Legend
    # plt.legend(
    #     bbox_to_anchor=(1.5,1),
    #     loc='upper left',
    #     borderaxespad=0
    # )
    # Show
    plt.show()
