#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [num for num in num_list if num % 2 == 0]
    print(num_list)
    return num_list

return_evens(num_list=range(1,10,2))

def make_exclamation(sentence_list):
    new_list = [sentence + '!' for sentence in sentence_list]
    print (new_list)
    return new_list
make_exclamation([])