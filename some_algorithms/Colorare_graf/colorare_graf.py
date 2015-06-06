"""
	Se da un poligon cu N laturi. El este impartit in triunghiuri prin N-3 diagonale.
	Diagonalele se citesc. Sa se coloreze laturile si diagonalele cu 2 culor diferite,
	astfel incat fiecare triunghi sa aiba laturi colorate cu ambele culori
"""

def main():
	# citire diag:
	st, en = [], []
	nr = 0
	while True:
		start = int(input("Start: "))
		if start == -1:
			break
		end = int(input("End: "))
		st.append(start)
		en.append(end)
		nr += 1

	nr_noduri = nr + 3

	# listele de vecini
	vecini = [[0] * (nr_noduri + 1) for _ in range(nr_noduri + 1)]

	# construim muchiile poligonului
	for i in range(1, nr_noduri + 1):
		if i < nr_noduri:
			vecini[i][i+1] = vecini[i + 1][i] = 1
		else:
			vecini[1][nr_noduri] = vecini[nr_noduri][1] = 1

	# adaugam diagonalele:
	for i in range(len(st)):
		vecini[st[i]][en[i]] = vecini[en[i]][st[i]] = 1

	culoare = 1 # consideram 1 = rosul si -1 = verde
	
	# pornim colorarea din nodul 1
	C = []
	vizitat = [False for _ in range(nr_noduri + 1)]

	C.append(1) 
	while C:
		curent = C.pop()
		vizitat[curent] = True
		for i in range(1, nr_noduri + 1):
			if vecini[curent][i] == 1:
				if not vizitat[i]:
					C.append(i)
					print str(curent) + "<->" + str(i) + "cu culoarea" + str(culoare)
					culoare *= -1

if __name__ == '__main__':
	main()