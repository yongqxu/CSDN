
from random import randint

dataset = {}

for i in range(1000):
    dataset.setdefault(randint(0,99), randint(1000, 100000));

counter = 0;
for key, value in dataset.items():
    sepp = ''
    if counter % 10 == 0:
        sepp = '\n'
    print(" {} = {}".format(key, value), end=sepp)
    counter += 1
print("\ntotal {}".format(counter))