import random

def gernerate_palindrome(length=100):
    if length % 2 != 0:
        raise ValueError('Die Laenge muss gerade sein, um ein Palindrom zu erstellen.')
    
    # Index at half length
    half_length = length // 2
    
    # Generate random character from the alphabet
    # random_chars = random.choices(string.ascii_letters + string.digits, k=half_length)
    random_chars = random.choices(['A', 'C', 'T', 'G'], k=half_length)

    # Generate palindrome
    palindrome = ''.join(random_chars) + ''.join(reversed(random_chars))
    
    return palindrome

def get_compl(seq):
    # Generate the complement of a DNA sequence
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
    # Check if the given sequence is palindromic
    return seq == get_compl(seq[::-1])  # return seq == seq[::-1] # distractor

def longest_palindrome(dna, start, end, longest_seq=''):

    # Base case: If the starting index exceeds the end of the sequence
    if start >= end:
        return longest_seq

    # Check all possible subsequences (minimum length 2)
    for length in range(2, end - start + 1):
        subseq = dna[start:start + length]  # subseq = dna[start:length] # distractor
        compl = get_compl(subseq)

        if is_palindromic(subseq) or subseq == compl:
            if len(subseq) > len(longest_seq):
                longest_seq = subseq

    # Recursive call for the next starting index
    return longest_palindrome(dna, start + 1, end, longest_seq)

# Example DNA sequence
# dna_sequence = "AGCTTAGCAGCTCGAATTCG"
# dna_sequence = "GTAACTCATGAGTTAC"
dna_sequence = "XCTAGXXCTAGX"

_dna_sequence = get_compl(dna_sequence)
print(dna_sequence)
print(_dna_sequence)
# dna_sequence = "XXCTAGXCTAGXX"
palindromic_sequences = longest_palindrome(dna_sequence, 0, len(dna_sequence))
print("Palindromische Sequenzen:", palindromic_sequences)
