s = input('input a string: ')
while True:
    subs = input('input a sub string: ')
    if len(subs) == 0:
        break
    print('Found \'{}\' in \'{}\' {} times'.format(subs, s, s.count(subs)))
