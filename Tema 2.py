f = open("date2.in")
nr_noduri = int(f.readline())

nr_alfabet = int(f.readline())
alfabet = f.readline()
alfabet = alfabet[:-1].split(" ")

q0 = f.readline()
q0 = q0[:-1]

nr_stari_fin = int(f.readline())
cin = f.readline().split(" ")
stari_finale = []
for i in range(nr_stari_fin):
    stari_finale.append(int(cin[i]))

nr_drumuri = int(f.readline())
drumuri = []
for i in range(nr_drumuri):
    inceput = f.readline()
    inceput = inceput[:-1].split(" ")
    drumuri.append(inceput)

mat = [[[] for i in range(nr_noduri)] for j in range(nr_alfabet)]
cnt = 0
for litera in alfabet:
    for j in range(nr_drumuri):
        if litera in drumuri[j][1]:
            mat[cnt][int(drumuri[j][0])].append(int(drumuri[j][2]))
    cnt += 1
print()
print('matricea:', mat)

cnt = 0
pas1 = [[] for i in range(nr_noduri)]
for i in range(nr_noduri):
    pas1[cnt].append(cnt)
    aux = cnt
    for j in mat[nr_alfabet - 1][cnt]:
        pas1[cnt].append(j)
        cnt = j
        for j in mat[nr_alfabet - 1][cnt]:
            pas1[aux].append(j)
            cnt = j
            for j in mat[nr_alfabet - 1][cnt]:
                pas1[aux].append(j)
                cnt = j
        cnt = aux
    cnt += 1
    '''while v[m - 1][cnt]:
        for j in v[m - 1][cnt]:
            lam[cnt].append(j)
            cnt = j
    cnt = aux
    cnt += 1'''

for i in pas1:
    x = len(i)
    j = 0
    while j <= x:
        ok = 1
        for y in i[j+1:]:
            if y == i[j]:
                i.remove(y)
                ok = 0
                break
        if ok:
            j += 1
for i in pas1:
    i = i.sort()
print()
print('pasul 1:', pas1)

pas2col2 = [[[[] for i in range(nr_noduri)] for j in range(nr_noduri)] for y in range(nr_alfabet - 1)]
for i in range(nr_noduri):
    litera = 0
    while litera < nr_alfabet - 1:
        cnt = 0
        for nod in pas1[i]:
            for x in mat[litera][nod]:
                pas2col2[litera][i][cnt] = x
                cnt += 1
        litera += 1
for litera in range(nr_alfabet - 1):
    for nod in range(nr_noduri):
        y = 0
        while y < nr_noduri:
            ok = 1
            for i in pas2col2[litera][nod][y + 1:]:
                if i == pas2col2[litera][nod][y]:
                    pas2col2[litera][nod].remove(i)
                    ok = 0
                    break
                if i == []:
                    pas2col2[litera][nod].remove(i)
                    ok = 0
                    break
            if ok:
                y += 1
print()
print('pasul 2, col. 2, a:', pas2col2[0])
print('pasul 2, col. 2, b:', pas2col2[1])

pas2col3 = [[[[] for i in range(100)] for j in range(nr_noduri)] for y in range(nr_alfabet - 1)]
for litera in range(nr_alfabet - 1):
    for nod in range(nr_noduri):
        cnt = 0
        for i in pas2col2[litera][nod]:
            if i or i == 0:
                for j in pas1[i]:
                    pas2col3[litera][nod][cnt] = j
                    cnt += 1
for litera in range(nr_alfabet - 1):
    for nod in range(nr_noduri):
        y = 0
        while y < nr_noduri:
            ok = 1
            for i in pas2col3[litera][nod][y + 1:]:
                if i == pas2col3[litera][nod][y]:
                    pas2col3[litera][nod].remove(i)
                    ok = 0
                    break
                if i == []:
                    pas2col3[litera][nod].remove(i)
                    ok = 0
                    break
            if ok:
                y += 1
for litera in range(nr_alfabet - 1):
    for i in pas2col3[litera]:
        i = i.sort()
print()
print('pasul 2, col. 3, a:', pas2col3[0])
print('pasul 2, col. 3, b:', pas2col3[1])

pas4 = [[[[] for i in range(nr_noduri)] for j in range(nr_noduri)] for y in range(nr_alfabet - 1)]
noduri_de_sters = [[] for i in range(nr_noduri)]
nr_noduri_noi = nr_noduri
nod_curent = 0
litera_curenta = 0
cnt = 0
while nod_curent < nr_noduri_noi - 1:
    nod = nod_curent + 1
    ok = 1
    while nod < nr_noduri_noi:
        ok1 = 0
        if pas2col3[litera_curenta][nod_curent] == pas2col3[litera_curenta][nod]:
            for i in stari_finale:
                if i in pas2col3[litera_curenta][nod]:
                    ok1 = 1
            litera = litera_curenta + 1
            while litera < nr_alfabet - 1:
                if pas2col3[litera][nod_curent] == pas2col3[litera][nod]:
                    for i in stari_finale:
                        if (i in pas2col3[litera][nod] and ok1) or (i not in pas2col3[litera][nod] and not ok1):
                            noduri_de_sters[nod_curent].append(nod + cnt)
                            del (pas2col3[litera_curenta][nod])
                            del (pas2col3[litera][nod])
                            nr_noduri_noi -= 1
                            cnt += 1
                            ok = 0
                            break
                litera += 1
        nod += 1
    if ok:
        nod_curent += 1
nr_noduri = len(pas2col3[0])
for i in range(nr_noduri):
    if noduri_de_sters[i]:
        litera = 0
        while litera < nr_alfabet - 1:
            nod = 0
            while nod < nr_noduri:
                n = len(pas2col3[litera][nod])
                for j in range(n):
                    if pas2col3[litera][nod][j] in noduri_de_sters[i]:
                        pas2col3[litera][nod][j] = i
                nod += 1
            litera += 1
for litera in range(nr_alfabet - 1):
    for nod in range(nr_noduri):
        y = 0
        while y < nr_noduri:
            ok = 1
            for i in pas2col3[litera][nod][y + 1:]:
                if i == pas2col3[litera][nod][y]:
                    pas2col3[litera][nod].remove(i)
                    ok = 0
                    break
                if i == []:
                    pas2col3[litera][nod].remove(i)
                    ok = 0
                    break
            if ok:
                y += 1
for litera in range(nr_alfabet - 1):
    for i in pas2col3[litera]:
        i = i.sort()
print()
print('pasul 4, a:', pas2col3[0])
print('pasul 4, b:', pas2col3[1])
