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

from visualizations.get_df_houses import get_df_houses
import visualizations.display_hist as dh
import mylib.math as myMath
import sys


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
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses('ressources/dataset_train.csv')
    # Show all option
    if is_show_all():
        dh.display_histograms(df_houses)
    # Display the Histogram of the homogenous course (Arithmancy)
    dh.display_arithmancy_histogram(df_houses)


# Launch the program
histogram()