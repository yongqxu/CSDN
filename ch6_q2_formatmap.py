
while True:
    n = input('input a string: ')
    if len(n) == 0:
        break
    data = {}
    index = 0
    s1 = ''
    number =''
    for i in range(len(n)):
        if ord(n[i]) in range(48, 57):
            number += n[i]
        else:
            if len(number) > 0:
                s1 += '{{number{}:010}}'.format(index)  ##build template for map keys
                data['number' + str(index)] = int(number)
                index += 1
                number = ''
            s1 += n[i]
    ##when input string ends with digits
    if len(number) > 0:
        s1 += '{{number{}:010}}'.format(index)
        data['number' + str(index)] = int(number)
    print(s1)
    print(s1.format_map(data))
