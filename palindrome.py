import random
import string

def gernerate_palindrome(length=100):
    if length % 2 != 0:
        raise ValueError("Die Länge muss gerade sein, um ein Palindrom zu erstellen.")
    
    # Berechne die Hälfte der Länge
    halfLen = length // 2
    
    # Generiere zufällige Zeichen aus dem Alphabet
    randomChars = random.choices(string.ascii_letters + string.digits, k=halfLen)

    # Erstelle das Palindrom
    palindrome = ''.join(randomChars) + ''.join(reversed(randomChars))
    
    return palindrome

def remove_char(str, n):
    # Überprüfen, ob n innerhalb der Grenzen der Zeichenkette liegt
    if n < 0 or n >= len(str):
        return "Index out of bounds!"
    
    # Zeichen an der Stelle n entfernen
    return str[:n] + str[n+1:]

def is_palindrome(sequence, left=0, right=-1):
    if left >= right:
        return True
    if sequence[left] != sequence[right]:
        return False

    return is_palindrome(sequence, left + 1, right - 1)

print(is_palindrome(gernerate_palindrome()))