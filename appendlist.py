arr = []
while True:
    n = input('input a number: ')
    if len(n) == 0:
        #arr.sort(reverse=True)
        print(sorted(arr, reverse=True))
        break
    n = int(n)
    arr.append(n)
