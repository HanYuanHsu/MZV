from ari import ALPHABET_SIZE

# given `word`, f maps a letter to another letter in the alphabet
# f is shuffle-invariant
# word is a monomial/tuple. 
# l is a letter in the alphabet
def f(word, l):
    word_sum = 0
    for i in word:
        word_sum += i
    
    return (l + word_sum) % ALPHABET_SIZE

# given `l`, phi maps a word to another word of the same length
# phi preserves shuffle
# l is a letter in the alphabet
# word is a monomial/tuple
def phi(l, word):
    output_list = []
    for d in word:
        output_list.append(phi_single(l, d))
    
    output = tuple(output_list)
    return output

# given `l`, phi_single maps a letter to another letter
# l, d are both letters  
def phi_single(l, d):
    return (d - l) % ALPHABET_SIZE