# 20 write a function that takes a number as argument and returns list of even and odd  number upto that number without using range

def even_odd_numbers_up_to(n):
    even_numbers = []
    odd_numbers = []
    num = 0
    while num <= n:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
        num += 1
    return even_numbers, odd_numbers

number = int(input("Enter a number: "))
even, odd = even_odd_numbers_up_to(number)
print("Even numbers up to", number, "are:", even)
print("Odd numbers up to", number, "are:", odd)
