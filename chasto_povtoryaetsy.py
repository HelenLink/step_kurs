with open(r'''C:\Users\ями\Desktop\dataset_3363_3.txt''') as f:
    k = f.read().replace('\n', ' ').lower().split()

max_val = max([k.count(i) for i in set(k)])
m = {i: k.count(i) for i in set(k) if k.count(i) == max_val}
print(sorted(m)[0], m[sorted(m)[0]])
sorted(m)

