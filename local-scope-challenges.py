# Thayer Yang
# 13 JAN 2025
# Local Scope Challenges

def greet(fname):
    print(f"Hello {fname.title()}")

def count_vowels(word):
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1

    return count
            
name = "Tom"

greet(name)
count_vowels(name)

print