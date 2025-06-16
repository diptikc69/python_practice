# 17 write a function that takes a string as a argument and returns the total number of vowels present in string

def count_vowel (word):
    lowered = word.lower()
    vowels = 'aeiou'
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] in vowels:
            count += 1
    if count >= 1:
         print(f'Total no. of vowels are {count}')
    else:
        print('No vowels')
