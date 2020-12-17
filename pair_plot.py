# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/17 05:53:20 by obelouch          #+#    #+#              #
#    Updated: 2020/12/17 23:32:36 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def     pair_plot():
    '''
     Displays a pair plot
    '''
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
        hue= "Hogwarts House",
        palette= houses_palette,
        plot_kws= {
            'alpha':0.4,
            's': 5
        },
        corner=True,
        height= 1.1,
    )
    # Show
    plt.show()


# Launch program
pair_plot()