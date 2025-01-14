# Thayer Yang
# 13 JAN 2025
# Local Scope Challenges

def greet(fname):
    print(f"Hello {fname.title()}")

def count_vowels(word):
    count = 0
    vowels = "aeiou"
    for char in word:
        if char in vowels:
            count += 1

    return count
            


greet("tim")

print(count_vowels("loop"))