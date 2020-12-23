# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/17 05:53:20 by obelouch          #+#    #+#              #
#    Updated: 2020/12/18 04:31:46 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.consts import bcolors
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys


def     exit_usage():
    '''
    Print the error Msg and Exit 
    '''
    print(f'\n{bcolors.FAIL}Error{bcolors.ENDC}: ', end='')
    print('Wrong number of arguments!')
    print(f'\n{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 pair_plot.py')
    exit(1)


def     pair_plot():
    '''
     Displays a pair plot
    '''
    if len(sys.argv) > 1:
        exit_usage()
    # Read dataframe from the CSV file
    df = pd.read_csv(
        'ressources/dataset_train.csv',
        # Columns to include
        usecols=[1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    )
    # Houses color palette
    houses_palette = {
        'Gryffindor':'#FF0000',
        'Ravenclaw':'#0000FF',
        'Hufflepuff':'#CCCC00',
        'Slytherin':'#00FF00',
    }
    # Set the theme of the subplots
    sns.set_theme(font_scale=0.52)
    # Pair Plot using 'Seaborn'
    sns.pairplot(
        data= df,
        #diag_kind="hist",
        hue= "Hogwarts House",
        palette= houses_palette,
        plot_kws= {
            'alpha':0.4,
            's': 5
        },
        height= 1.1,
    )
    # Show
    plt.show()


# Launch program
pair_plot()