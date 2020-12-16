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

from visualizations.display_scatter import display_scatter_2f
from visualizations.get_df_houses import get_df_houses
import mylib.math as myMath
import sys

# Global Variables:
COURSE1 = 'Arithmancy'
COURSE2 = 'Astronomy'

def     is_show_all():
    '''
    Test if the detail flag is present
    '''
    
    if sys.argv[1] == '-d' or sys.argv[1] == '--details':
        return True
    return False


def     pick_features():
    '''
    Pick the features to scatter if the syntax is correct
    '''
    if len(sys.argv) != 2:
        print('error')
        exit(1)
    if ()
    


def     scatter_plot():
    '''
    displays a scatter plot That show thee 2 features that are similar
    '''
    if len(sys.argv) > 1:
        pick_features()
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses('ressources/dataset_train.csv')
    # Display the Scatter of the 2 similar features
    display_scatter_2f(df_houses, COURSE1, COURSE2)


# Launch the program
scatter_plot()