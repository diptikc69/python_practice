grade={
    'ram':85,
    'shyam':62,
    'hari':55,
    'ramesh':25
}
name=input('Enter name').lower()
if name in grade:
    marks=grade[name]
    print(f'Hi{name.capitalize()}.your grade is {marks}')
else:
    print('Name not found')