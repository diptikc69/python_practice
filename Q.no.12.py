# 12 write a function that takes multiple number and return maximum of those number

def max_num(list):
    max_num = 0

    for i in list:
        if i > max_num:
            max_num = i
    print(max_num)


