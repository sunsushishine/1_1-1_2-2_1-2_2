import codecs

sort_arr = []
with open('unsort.txt', encoding = 'utf-8', mode = 'r') as content:
    lines = content.readlines()
    
for line in lines:
    sort_arr.append(line.strip())
    
sort_arr.sort()
with open('sorted.txt','w') as output:
    for i in sort_arr:
        output.write(i+'\n')
#print(sort_arr)
