import os
import os.path
lines = []
with open('tree.txt', 'w') as f:
    for root, dir_names, files in os.walk('main'):
        for file in files:
            if file.endswith('.py'):
                # for line in open(os.path.join(list(root, files))):
                # lines = lines.append(root)
                f.write(root +'\n')

                break
