with open(r'''C:\Desktop\python\dataset_3380_5.txt''') as f:
   a = f.readlines()
#ls = [row.strip().split('\t')[::2] for row in a]
ls = [row.strip().split('\t') for row in a]
d = {}
for i in ls:
    d.setdefault(int(i[0]), []).append(int(i[2]))
print(d)
for i in range(1, 12):
    if i not in d:
        d[i] = '-'
for k, v in sorted(d.items()):
    print(*(k, sum(v)/len(v)) if str(d[k][0]).isdigit() else (k, '-'))