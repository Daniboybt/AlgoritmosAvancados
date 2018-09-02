def transformaInt(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])

def binarySearch(lista, element, left, right):
	pivo = (right + left) // 2
		
	if element == lista[pivo]:
		return pivo
        
	elif right <= left:
		return -1
			
	elif element < lista[pivo]:
		return binarySearch(lista, element, left, pivo - 1)
        
	else:
		return binarySearch(lista, element, pivo + 1, right)

def interativeBinarySearch(lista, element, left, right):
	
	inf = left
	sup = right
	while (inf <= sup):
		meio = (inf + sup)//2;
		
		if (element == lista[meio]):
			return meio;
		if (element < lista[meio]):
			sup = meio-1
		else:
			inf = meio+1
	return -1

numCasos = input().split()
transformaInt(numCasos)
casos = 1

while(numCasos[0] != 0 and numCasos[1] != 0):
	
	pecas = []
	for i in range(numCasos[0]):
		peca = int(input())
		pecas.append(peca)
		
	pecas = sorted(pecas)
	print("CASE# %d:" % (casos))
	
	for i in range(numCasos[1]):
		consulta = int(input())
		
		res = interativeBinarySearch(pecas, consulta, 0, len(pecas) - 1)
		if res != -1:
			while(res > 0):
				if pecas[res] == pecas[res - 1]:
					res -= 1
				else:
					break	
			
			print("%d found at %d" %(consulta, res + 1))
			
		else:
			print ("%d not found" % consulta)
	numCasos = input().split()
	transformaInt(numCasos)
	casos += 1
