import itertools

lst = [1, 2, 3]
hoan_vi = list(itertools.permutations(lst))

print("Tất cả các hoán vị của [1, 2, 3]:")
for hv in hoan_vi:
    print(hv)
