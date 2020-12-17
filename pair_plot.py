# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/17 05:53:20 by obelouch          #+#    #+#              #
#    Updated: 2020/12/17 06:19:42 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from visualizations.display_pairPlot import display_pairPlot
from visualizations.get_df_houses import get_df_houses
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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
    # Pair Plot using 'Seaborn'
    sns.pairplot(
        data= df,
        hue= "Hogwarts House",
        palette= houses_palette,
        plot_kws= {
            'alpha':0.4,
            's': 5
        },
        height= 2,
    )
    plt.suptitle('Courses pair plot')
    # Show
    plt.show()


# Launch program
pair_plot()