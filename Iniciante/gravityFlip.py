def transformaInt(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
		
numColunas = int(input())
cubos = input().split()
transformaInt(cubos)

for i in range(len(cubos) - 1, 0, -1):
	j = i
	while(cubos[j - 1] > cubos[j]): 
		diferenca = cubos[j - 1] - cubos[j]
		cubos[j - 1] -= diferenca
		cubos[j] += diferenca
		
		j += 1
		if(j == len(cubos)):
			break

print(*cubos, sep=" ")
print()
