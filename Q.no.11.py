# 11 write a function that takes list of numbers as argument  and return list of number with only even number

list = [1, 2, 3, 4, 5, 8, 9, 16]

def even_only_list(list):
    list2 = []
    for i in list:
        if i % 2 == 0:
            list2.append(i)
    print(list2)
even_only_list(list)