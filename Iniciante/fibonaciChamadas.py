def fibonaci(num, lista):
	if num == 0:
		return [0, 1]
	if num == 1:
		return [1, 1]
	
	for i in lista:
		if i[0] == num:
			return i[1]
	
	else:
		res1 = fibonaci(num - 1, lista)
		res2 = fibonaci(num - 2, lista)
		
		res = [num]
		res.append([res1[0] + res2[0], res1[1] + res2[1] + 1])
		
		lista.append(res)
		return res[1]
				
numCasos = int(input())
casos = []
 
for i in range(numCasos):
	caso = int(input())
	resultado = fibonaci(caso, casos)
	
	print("fib(%d) = %d calls = %d" %(caso, resultado[1] - 1, resultado[0]))

print(*casos, sep=" ")
