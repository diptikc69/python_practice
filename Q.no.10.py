# 10 write a function that takes string as argument whether letter u is present or not

def present(s):
    for char in s:
        if char == 'u':
            return True
    return False


userInput = input("Enter a string: ")
if present(userInput):
    print("The letter 'U' is present in the string.")
else:
    print("The letter 'U' is not present in the string.")
