cartas = input().split()
cartaA = int(cartas[0])
cartaB = int(cartas[1])

if cartaA == cartaB:
	print(cartaA)
elif cartaA < cartaB:
	print(cartaB)
else:
	print(cartaA)
