
while True:
    cmd = input('>>> ')
    if cmd == '':
        print('Bye\n')
        break
    print('>>>', eval(cmd))
