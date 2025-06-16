# 9 write a function that takes string as argument the count of the letter U present in the string without using count disregarding case sensitive

def countU(s):
    count = 0
    for char in s:
        if char.lower() == 'u':
            count += 1
    return count

userInput = input("Enter a string: ")
Ucount = countU(userInput)
print(f"The count of the letter {Ucount} is in the string")
