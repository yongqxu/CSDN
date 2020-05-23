lines = 5
for i in range(lines+1):
    left = [' ']*(lines-i)
    stars = ['*']*(2*i+1)
    print(left + stars+ left, sep='')
