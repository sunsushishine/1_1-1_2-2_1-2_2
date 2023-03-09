import urllib.request
lst = list()
with urllib.request.urlopen('http://dfedorov.spb.ru/python3/src/romeo.txt') as webpage:
        for i in webpage:
            i = i.decode('utf-8')
            i = i.strip()
            for word in i.split():
                lst.append(word)

word_count = {}
for word in lst:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word} --> {count}")

#print(lst)    
