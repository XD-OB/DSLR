# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    libft.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/23 19:52:21 by obelouch          #+#    #+#              #
#    Updated: 2020/12/23 19:52:21 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def     get_flags_and_args():
    '''
    Get Args & Flags (without -) from the ARGV
    '''
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
    flags = [arg[1:] for arg in sys.argv[1:] if not arg in args]
    return (flags, args)
