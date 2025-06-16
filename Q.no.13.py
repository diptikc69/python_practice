#13 write a function that takes a string as a argument and check whether vowels are present
def vowels(s):
    vowel = "aeiouAEIOU"  
    for char in s:
        if char in vowel:
            return True
    return False

userInput = input("Enter a string: ")
if vowels(userInput):
    print("The  contains vowels.")
else:
    print("The string does not contain any vowels.")
