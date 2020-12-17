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


def     pair_plot():
    '''
     Displays a pair plot
    '''
    # get dictionary of dataframes from a csv file
    df_houses = get_df_houses('ressources/dataset_train.csv')
    # Display the pair plot of the houses dataframe
    display_pairPlot(df_houses)


# Launch program
pair_plot()