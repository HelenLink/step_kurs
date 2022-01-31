with open(r'''C:\Users\dataset_3363_4.txt''', encoding= ' utf-8') as f:
    k = f.readlines()

ocenki = [row.strip().split(';')[1:] for row in list(k)]
for elem in ocenki:
    print(sum(map(int, elem))/len(elem))
sr_m = sum([int(j[0]) for j in ocenki])/len(ocenki)
sr_f = sum([int(j[1]) for j in ocenki])/len(ocenki)
sr_r = sum([int(j[2]) for j in ocenki])/len(ocenki)
print(sr_m, sr_f, sr_r)
