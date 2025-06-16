# 19 write a function that takes a number and returns list of even number upto that number without using range

def even_numbers_up_to(n):
    even_numbers = []
    num = 0
    while num <= n:
        if num % 2 == 0:
            even_numbers.append(num)
        num += 1
    return even_numbers

number = int(input("Enter a number: "))
result = even_numbers_up_to(number)
print("Even numbers up to", number, "are:", result)
