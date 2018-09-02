def transformaInt(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
		
def bb(lista, element, inicio, fim):
	m = (inicio+fim)//2
	if inicio == fim:
		return m
	if lista[m] <= element:
		 return bb(lista, element, m+1, fim)
	elif lista[m] > element:
		return bb(lista, element, inicio, m)	

numSizes = input().split()

arrayA = input().split()
arrayB = input().split()

transformaInt(arrayA)
arrayA = sorted(arrayA)
valores = []

for i in range(len(arrayB)):
	arrayB[i] = int(arrayB[i])
	valor = bb(arrayA, arrayB[i], 0, len(arrayA))
	#while(valor < len(arrayA)):
		#if arrayA[valor] <= arrayB[i]:
		#	valor += 1
		#else:
		#	break
	print(valor, end= " ")
print()
