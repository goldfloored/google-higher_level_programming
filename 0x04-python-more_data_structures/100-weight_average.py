#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    average = 0
    somme = 0
    for couple in my_list:
        average += (couple[0] * couple[1])
        somme += couple[1]
    return (average / somme)
