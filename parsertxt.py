# %%

import json

data = []

text = open('fido7.nsk.general.txt').readlines()
for line in text:
    if line == '\n':
        continue
    try:
        line = line[:-5]
        # print(line)
        a = json.loads(line)
    except:
        # print('error')
        continue

    # break
    tmp = []
    for b in a:
        try:
            if b[2] != None:
                tmp.append(b[2])
        except:
            pass
    tmp.sort(key=len)
    data.append(tmp[-1])

# %%

lst = []

for x in data:
    lst += [a[0][1] for a in json.loads(x)[0]]
    
len(set(lst))

# %%
