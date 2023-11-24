#!/usr/bin/env python3

def return_evens(num_list):
    even_integers = [i for i in num_list if i%2 == 0]
    return (even_integers)

#return_evens([1,2,3,4])

def make_exclamation(sentence_list):
    add_exclamation =[word + "!" for word in sentence_list]
    return (add_exclamation)

#make_exclamation(["hello", "world"])

