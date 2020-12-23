# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display_scatter.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/25 12:41:15 by obelouch          #+#    #+#              #
#    Updated: 2020/12/17 05:52:37 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
from numpy import isnan


def     get_house_courses(df_houses, house, course1, course2):
    '''
    Get a Dataframe of 2 columns (course1, course2) and return a Dictionary of course1 & course2
    without NaNs values
    '''
    # Select the 2 columns from the house dataframe
    col1 = df_houses[house].loc[:, course1]
    col2 = df_houses[house].loc[:, course2]
    # Clean indexs
    indexs = [(~isnan(x) and ~isnan(y)) for x, y in zip(col1, col2)]
    # Remove the lines that contain a NaN Value
    courses = {
        course1: list(col1[indexs]),
        course2: list(col2[indexs]),
    }
    return courses


def     display_scatter_2f(df_houses, f1, f2):
    '''
    Display Scatter plot of the 2 features passed in arguments
    '''
    # Get Courses:
    course1 = df_houses['R'].columns[f1]
    course2 = df_houses['R'].columns[f2]
    # Init Figure
    figure = plt.figure(figsize=(10,8))
    # Set Window Title
    figure.canvas.set_window_title(f'Scatter of the courses  " {course1} " and " {course2} "')
    ###### Ravenclaw Scatter
    courses = get_house_courses(df_houses, 'R', course1, course2)
    plt.scatter(
        courses[course1],
        courses[course2],
        alpha=0.4,
        color='#0000FF',
        label='Ravenclaw',
    )
    ###### Hufflepuff Scatter
    courses = get_house_courses(df_houses, 'H', course1, course2)
    plt.scatter(
        courses[course1],
        courses[course2],
        alpha=0.5,
        color='#CCCC00',
        label='Hufflepuff',
    )
    ###### Gryffindor Scatter
    courses = get_house_courses(df_houses, 'G', course1, course2)
    plt.scatter(
        courses[course1],
        courses[course2],
        alpha=0.4,
        color='#FF0000',
        label='Gryffindor',
    )
    ###### Slytherin Scatter
    courses = get_house_courses(df_houses, 'S', course1, course2)
    plt.scatter(
        courses[course1],
        courses[course2],
        alpha=0.4,
        color='#00FF00',
        label='Slytherin',
    )
    ############################
    plt.title(f'Scatter "{course1}" with "{course2}"')
    plt.legend(loc='upper right')
    plt.ylabel(course2)
    plt.xlabel(course1)
    # Adds major gridlines
    plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    # Show
    plt.show()
