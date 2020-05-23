
def sort_numbers(*numbers, type='asc'):
    nums = []
    for number in numbers:
        nums.append(int(number))
    if type != 'asc':
        return sorted(nums, reverse=True)
    else:
        return sorted(nums)

while True:
    data = input('input a list of comma separated numbers:')
    if len(data) == 0:
        break
    data = data.split(',')
    print('sorted ascending {}'.format(sort_numbers(*data)))
    print('sorted descending {}'.format(sort_numbers(*data, type='desc')))