f = open("date2.in")
n = int(f.readline())

m = int(f.readline())
alfabet = f.readline()
alfabet = alfabet[:-1].split(" ")

q0 = f.readline()
q0 = q0[:-1]

k = int(f.readline())
cin = f.readline().split(" ")
stari_finale = []
for i in range(k):
    stari_finale.append(int(cin[i]))

nr_drumuri = int(f.readline())
drumuri = []
for i in range(nr_drumuri):
    inceput = f.readline()
    inceput = inceput[:-1].split(" ")
    drumuri.append(inceput)

v = [[[] for i in range(n)] for j in range(m)]

cnt = 0
for j in alfabet:
    for i in range(nr_drumuri):
        if j in drumuri[i][1]:
            v[cnt][int(drumuri[i][0])].append(int(drumuri[i][2]))
    cnt += 1
print('matricea:', v)

cnt = 0
lam = [[] for i in range(n)]
for i in range(n):
    lam[cnt].append(cnt)
    aux = cnt
    for j in v[m - 1][cnt]:
        lam[cnt].append(j)
        cnt = j
        for j in v[m - 1][cnt]:
            lam[aux].append(j)
            cnt = j
            for j in v[m - 1][cnt]:
                lam[aux].append(j)
                cnt = j
        cnt = aux
    cnt += 1
    '''while v[m - 1][cnt]:
        for j in v[m - 1][cnt]:
            lam[cnt].append(j)
            cnt = j
    cnt = aux
    cnt += 1'''

for i in lam:
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
for i in lam:
    i = i.sort()
print('lambda inchiderea:', lam)

#w = [[set() for j in range(n)] for y in range(m-1)]
w = [[[[] for i in range(n)] for j in range(n)] for y in range(m-1)]
for i in range(n):
    aux = 0
    while aux < m-1:
        cnt = 0
        for j in lam[i]:
            for x in v[aux][j]:
                w[aux][i][cnt] = x
                #w[aux][i].add(x)
                cnt += 1
        aux += 1
for i in range(m-1):
    for j in range(n):
        y = 0
        while y < n:
            ok = 1
            for x in w[i][j][y + 1:]:
                if x == w[i][j][y]:
                    w[i][j].remove(x)
                    ok = 0
                    break
                if x == []:
                    w[i][j].remove(x)
                    ok = 0
                    break
            if ok:
                y += 1
print('tranzitie:', w)
