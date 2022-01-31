with open('1.txt') as f, open('out.txt', 'w') as w:
    w.writelines(f.readlines()[::-1])

