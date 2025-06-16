grade={
    'first':80,
    'second':70,
    'third':60,
    'fourth':50,
    'fifth':40
}
score=input('Enter grade').lower()
if score in grade:
    marks=grade[score]
    print(f'Hi {score.capitalize()}.your grade is {marks}')
else:
    print('Your are fail')