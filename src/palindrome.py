import random

# Generate random DNA (A,C,T,G) sequence of given length
def gernerate_dna_palindrome(length=100):
    if length % 2 != 0:
        raise ValueError('Die Laenge muss gerade sein, um ein Palindrom zu erstellen.')
    half_length = length // 2
    random_chars = random.choices(['A', 'C', 'T', 'G'], k=half_length)
    palindrome = ''.join(random_chars) + ''.join(reversed(random_chars))
    return palindrome

# Generate the complement of a DNA sequence
def get_compl(seq):
    complement = ''
    for base in seq:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
    return complement

def is_palindromic(seq):
    return seq == get_compl(seq[::-1])  # return seq == seq[::-1] #distractor

def longest_palindrome(dna, start, end, longest_seq=''):

    if start >= end:  # if start < end: #distractor
        return longest_seq  # return '' #distractor

    for length in range(2, end - start + 1):
        subseq = dna[start:start + length]  # subseq = dna[start:length] #distractor

        if is_palindromic(subseq):
            if len(subseq) > len(longest_seq):
                longest_seq = subseq  # return subseq #distractor

    return longest_palindrome(dna, start + 1, end, longest_seq)  # return longest_palindrome(dna, start + 1, end - 1, longest_seq) #distractor

# Example DNA sequences
# dna_sequence = "AGCTTAGCAGCTCGAATTCG"
dna_sequence = "GTAACTCATGAGTTAC"
# dna_sequence = "XCTAGXXXCTAGX"
# dna_sequence = "TAT"
# dna_sequence = "CC"
# dna_sequence = ""
# dna_sequence = gernerate_dna_palindrome()

print(dna_sequence)
print(get_compl(dna_sequence))
palindromic_sequences = longest_palindrome(dna_sequence, 0, len(dna_sequence))
print("Längste Palindromische Sequenzen:", palindromic_sequences)