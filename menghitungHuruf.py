test: str = input("Masukkan Kalimat : ")

dic = {}
for x in test:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for data in dic:
    print('huruf ', data, ' : ', dic[data])
