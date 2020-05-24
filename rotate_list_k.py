
def rotate_k_list(a, k):
    if k == 0:
        return a
    k %= len(a)
    subl1 = a[:k]
    subl2 = a[k:]
    subl2.extend(subl1)
    return subl2


alist = [1, 2, 3, 4, 5, 6]
print(rotate_k_list(alist, 2))

print(rotate_k_list(alist, 5))

print(rotate_k_list(alist, 1))