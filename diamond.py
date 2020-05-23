
while True:
    n = input('give number of lines (odd number): ')
    if len(n) == 0:
        print('Bye\n')
        break
    n = int(n)
    if n % 2 == 0:
        print('it has to be odd number, please try input it again.')
        continue
    m = n//2
    for i in range(n):
        if i <= m:
            print(' '*(m-i), sep='', end='')
            print('*'*(i*2+1), sep='', end='')
            print()
        else:
            print(' '*(i-m), sep='', end='')
            print('*'*((n-1-i)*2+1), sep='', end='')
            print()
