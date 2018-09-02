def transformaInt(lista):
	for i in range(len(lista)):	
		lista[i] = int(lista[i])

count = 1	
numRodadas = int(input())

while(numRodadas != 0):	
	beto = 0
	aldo = 0
	count = 1
	
	for i in range(numRodadas):
		rodada = input().split(" ")
		transformaInt(rodada)
	
		aldo += rodada[0]
		beto += rodada[1]

	print("Teste %d" %count)
	if aldo > beto:
		print ("Aldo")
	else:
		print ("Beto")
	print()
	
	count += 1
	numRodadas = int(input())
