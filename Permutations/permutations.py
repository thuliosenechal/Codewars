'''
In this kata you have to create all permutations of an input string and
remove duplicates, if present. This means, you have to shuffle all 
letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

'''

import itertools


def permutations(string):
    lista = [''.join(anagrama) for anagrama in itertools.permutations(string)]
    return sorted(set(lista)) 


if __name__ == '__main__':
    print(permutations('aabb'))
    