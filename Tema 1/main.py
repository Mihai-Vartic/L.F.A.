def verificare(sir):
    inceput = [q0]
    lungime_curenta = 0
    lungime_cuvant = len(sir)
    while lungime_curenta < lungime_cuvant:
        urmator = []
        for nod in inceput:
            for drum_curent in range(nr_drumuri):
                if nod == drumuri[drum_curent][0]:
                    if drumuri[drum_curent][1] == sir[lungime_curenta]:
                        urmator.append(drumuri[drum_curent][2])
                        inceput = urmator
                    elif drumuri[drum_curent][1] == '$':
                        urmator.append(drumuri[drum_curent][2])
                        inceput.append(drumuri[drum_curent][2])
        if not urmator:
            print("FALSE")
            return
        lungime_curenta += 1
    if int(inceput[0]) in stari_finale:
        print("TRUE")
    else:
        print("FALSE")

f = open("date.in")
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

teste = []
nr_teste = int(f.readline())
for i in range(nr_teste):
    teste.append(f.readline().strip())

for sir in teste:
    print(sir)
    verificare(sir)
