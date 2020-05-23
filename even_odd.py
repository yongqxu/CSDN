
while True:
    num = input('input a number>>>')
    if num == '':
        print('Bye')
        break
    if int(num) % 2 == 0:
        print('num', num, 'is even')
    else:
        print('num', num, 'is odd')