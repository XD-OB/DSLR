# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_predict.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/24 00:42:54 by obelouch          #+#    #+#              #
#    Updated: 2020/12/24 00:42:54 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.consts import bcolors

def     show_result(predict_df, is_print):
    '''
    Show the result in a CSV file or in the terminal based on the flag
    '''
    if is_print == True:
        # Show the result
        ## Gryffindor:
        print(f'{bcolors.FAIL}------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Gryffindor'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.FAIL}--------- Gryffindor [{count}] ---------{bcolors.ENDC}\n')
        ## Hufflepuff:
        print(f'{bcolors.WARNING}-------------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Hufflepuff'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.WARNING}--------- Hufflepuff [{count}] ---------{bcolors.ENDC}\n')
        ## Ravenclaw
        print(f'{bcolors.OKBLUE}------------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Ravenclaw'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.OKBLUE}--------- Ravenclaw [{count}] ---------{bcolors.ENDC}\n')
        ## Slytherin
        print(f'{bcolors.OKGREEN}-----------------------------------{bcolors.ENDC}')
        count = 0
        for student in predict_df.loc[predict_df['Hogwarts House'] == 'Slytherin'].itertuples():
            print('%-4d: %s %s' % (student[0], student[2], student[3]))
            count += 1
        print(f'{bcolors.OKGREEN}---------- Slytherin [{count}] ---------{bcolors.ENDC}\n')
    else:
        try:
            # Write the result in a csv file:
            predict_df.to_csv(
                'houses.csv',
                index_label= 'Index',
                columns=['Hogwarts House']
            )
            # Print Finish message:
            print('\n%sSuccess:%s ' % (bcolors.OKGREEN, bcolors.ENDC) , end='')
            print('The prediction result is stored in %shouses.csv%s' % (bcolors.OKCYAN, bcolors.ENDC))
        except:
            print('\n%sFail:%s The prediction result is not stored!' % (bcolors.FAIL, bcolors.ENDC))
