import random
import string

def gernerate_palindrome(length=100):
    if length % 2 != 0:
        raise ValueError('Die Länge muss gerade sein, um ein Palindrom zu erstellen.')
    
    # Index at half length
    half_length = length // 2
    
    # Generate random character from the alphabet
    random_chars = random.choices(string.ascii_letters + string.digits, k=half_length)

    # Generate palindrome
    palindrome = ''.join(random_chars) + ''.join(reversed(random_chars))
    
    return palindrome

def remove_char(str, n):
    if n < 0 or n >= len(str):
        return 'Index out of bounds!'
    
    # Remove character at index n
    return str[:n] + str[n+1:]

def is_palindrome(sequence, left, right):
    if left >= right:
        return True
    if sequence[left] != sequence[right]:
        return False

    return is_palindrome(sequence, left + 1, right - 1)

sequence = 'AibohphobiA'
print(is_palindrome(sequence, 0, len(sequence) - 1))

# print(is_palindrome(gernerate_palindrome(), 0, 99))
