def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation:")
print("1.Addition")
print("2.Subtration")
print("3.Multiplication")
print("4.Divide")


choice=(input("enter choice(1/2/3/4)"))
num1=int(input("enter a first number:"))
num2=int(input(" enter a second number:"))
if choice =='1':
    print(add(num1,num2))
elif choice =='2':
    print(sub(num1,num2))
elif choice =='3':
    print(mul(num1,num2))
elif choice =='4':
    print(div(num1,num2))
else:
    print("Invalid number:")