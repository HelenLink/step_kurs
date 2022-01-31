with open(r'''C:\Desktop\text.txt''', encoding= ' utf-8') as f:
    k = f.readlines()

ocenki = [row.strip().split(';')[1:] for row in list(k)]

v = open(r'''C:\Desktop\fale1.txt''', 'w', encoding=' utf-8')
for elem in ocenki:
    a = sum(map(int, elem))/len(elem)
    v.write(str(a) + '\n')
sr_m = sum([int(j[0]) for j in ocenki])/len(ocenki)
sr_f = sum([int(j[1]) for j in ocenki])/len(ocenki)
sr_r = sum([int(j[2]) for j in ocenki])/len(ocenki)
#print(sr_m, sr_f, sr_r)
v.write(str(sr_m)+ ' ')
v.write(str(sr_f)+ ' ')
v.write(str(sr_r))
v.close()