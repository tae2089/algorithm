from itertools import permutations

def key(t):
    return int(t)

a = [3, 30, 34, 5, 9]
b = permutations(a,len(a))
num_list = []
for i in b:
    num_list.append("".join(map(str, i)))

print(sorted(num_list,key=key)[-1])


