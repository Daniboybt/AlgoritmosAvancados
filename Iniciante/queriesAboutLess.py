def transformaInt(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
		
def binarySearch(lista, element, left, right):
	if right - left > 1:
		pivo = (right + left) // 2
        
		if element == lista[pivo]:
			return pivo + 1
        
		elif element < lista[pivo]:
			return binarySearch(lista, element, left, pivo)
        
		else:
			return binarySearch(lista, element, pivo, right)

	else:
		return left

numSizes = input().split()

arrayA = input().split()
arrayB = input().split()

transformaInt(arrayA)
arrayA = sorted(arrayA)
valores = []

for i in range(len(arrayB)):
	arrayB[i] = int(arrayB[i])
	valor = binarySearch(arrayA, arrayB[i], 0, len(arrayA) - 1)
	while(valor < len(arrayA)):
		if arrayA[valor] <= arrayB[i]:
			valor += 1
		else:
			break
	print(valor, end= " ")
