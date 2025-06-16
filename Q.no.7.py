# 7 write a function that takes string as an argument and check if digit is present in the string

def  count(s):
    digit = ('1','2','3','4','5')
    for char in s:
        if char in s:
            return True
        else:
            return False
print(count('3'))


# def count(s):
#     digit = ('0','1','2','3','4','5','6','7','8')
#     for char in s:
#         if char in digit:
#             return True
#     return False

# userInput = input("Enter a string: ")
# print(count(userInput))

