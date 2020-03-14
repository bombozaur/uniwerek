wagi={}
nastepnicy_podstawowi={}
pary_do_obrobki=[]
caly_graf={}
krawedzie={}

def otwarcie_i_podstawowa_obrobka():
	f = open("graph.txt", "r")
	ilosc_wierzcholkow=f.readline()
	for x in range(int(ilosc_wierzcholkow)):
		wagi[x+1]=[]
		linia=f.readline().split()
		for y in linia:
			if y=="-":
				wagi[x+1].append(float('inf'))
			else:
				wagi[x+1].append(y)
	pary=f.readline().split()		
	while(pary):
		pary_do_obrobki.append(pary)
		pary=f.readline().split()
	f.close()

def nastepnicy(z,do):
	for x in z.keys():
		do[x]=[]
		for y in range(len(z[x])):
			if wagi[x][y] != float('inf'):
				do[x].append(y+1)


def zbiory_z_wagami(z,do,przez):
	for x in przez:
		do[x]={}
		for y in przez[x]:
			do[x][y]=z[x][y-1]


def krawedzie_z_wagami(z,do):
	for x in z:
		for y in range(len(z[x])):
			if z[x][y] != float('inf'):
				if x<(y+1):
					do[(x,y+1)]=z[x][y]
					# przy grafie skierowany mozna dodac warunek przeciwny, a tak tylko polowe macierzy przerabiamy by nie bylo powtorzen


def obrubka_z_nowymi_wagami(z,na):
	for x in z:
		for y in range(len(z[x])):
			for c in na:
				if (x==int(c[0]) and y+1==int(c[1])) or (x==int(c[1]) and y+1==int(c[0])):
					if z[x][y]==float('inf'):
						z[x][y]=3
					else:
						z[x][y]=float('inf')
					#dla grafu skierowanego wystraczy usunac ora

def print_nast(lista):
	print("Lista następników:")
	for x in lista:
		print(x,":", end=" ")
		for y in lista[x]:
			print(y, end=" ")
		print("",end="\n")

def print_all(nastepnicy_lista,caly_graf_lista,krawedzie_lista):
	print(nastepnicy_lista)
	print("----------------------------------------------")
	print(caly_graf_lista)
	print("----------------------------------------------")
	print(krawedzie_lista)
	print("----------------------------------------------")
	print_nast(nastepnicy_lista)
	print("----------------------------------------------")

otwarcie_i_podstawowa_obrobka()
nastepnicy(wagi,nastepnicy_podstawowi)
zbiory_z_wagami(wagi,caly_graf,nastepnicy_podstawowi)
krawedzie_z_wagami(wagi,krawedzie)
print_all(nastepnicy_podstawowi,caly_graf,krawedzie)

nastepnicy_podstawowi={}
caly_graf={}
krawedzie={}

obrubka_z_nowymi_wagami(wagi,pary_do_obrobki)
nastepnicy(wagi,nastepnicy_podstawowi)
zbiory_z_wagami(wagi,caly_graf,nastepnicy_podstawowi)
krawedzie_z_wagami(wagi,krawedzie)
print_all(nastepnicy_podstawowi,caly_graf,krawedzie)