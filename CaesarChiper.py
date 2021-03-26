code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
print('karakter yang dipakai =>',''.join([str(elem) for elem in code]))
shift:int = int(input('nilai shift ke kanan => '))
dataraw = input('pesan ==> ')
datas = []
for x in range(len(dataraw)):
    raws = dataraw[x]
    if dataraw[x] in code:
        idx = code.index(raws)
        newidx = idx+shift
        if newidx > 35:
            newidx -= 36
        datas.insert(x,code[newidx])
    else:
        datas.insert(x,raws)
print('pesan terenkripsi ==>',''.join([str(elem) for elem in datas]))
