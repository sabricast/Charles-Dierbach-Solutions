# Write a Python function named numVowels that is passed a string containing letters,
# each of which may be in either uppercase or lowercase, and returns a tuple containing
# the number of vowels and the number of consonants the string contains.


def numVowels(s):
    """
    Returns a tuple with the number of vowels and the number of consonants (in that order) of s.

    (str) -> (tuple)

    \>>> numVowels('Hello!') -> (2, 3)
    \>>> numVowels('Goodbye!') -> (3, 4)
    \>>> numVowels('My name is Sabrina') -> (6, 9)

    """
    s = s.lower()

    num_of_vowels = 0
    num_of_consonants = 0

    for char in s:
        if char in 'aeiou':
            num_of_vowels += 1
        elif char in 'bcdfghjklmnpqrstvwxyz':
            num_of_consonants += 1

    return num_of_vowels, num_of_consonants


# --- main


print(numVowels('Hello!'))
print(numVowels('Goodbye!'))
print(numVowels('My name is Sabrina'))
