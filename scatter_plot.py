# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/15 02:30:19 by obelouch          #+#    #+#              #
#    Updated: 2020/12/15 02:30:19 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

from visualizations.get_df_houses import get_df_houses
import visualizations.display_scatter as ds
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


def     scatter_plot():
    '''
    displays a scatter plot That show thee 2 features that are similar
    '''
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses('ressources/dataset_train.csv')
    # Show all option
    if is_show_all():
        ds.display_scatters(df_houses)
    # Display the Histogram of the homogenous course (Arithmancy)
    ##dh.display_arithmancy_histogram(df_houses)


# Launch the program
scatter_plot()