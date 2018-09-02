def transformaInt(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])

def avaliaRodada(jogadores, cartasRodada):
	perdedores = []
	menor = 0
	for i in range(len(cartasRodada)):
		if cartasRodada[i] < cartasRodada[menor]:
			perdedores = [i]
			menor = i
			
		elif cartasRodada[i] == cartasRodada[menor]:
			perdedores.append(i)
		
	if len(perdedores) == len(jogadores):
		return jogadores
		
	for indice in range(len(perdedores), -1, -1):
		jogadores.pop(indice)
	
	if(len(jogadores) == 1):
		return jogadores
		
	return []
	
def jogo(jogadores, cartas):
	listaCartas = 0
	i = 0 
	
	while(True):	
		countJogadores = 0
		cartasRodada = []
			
		while(i < len(cartas[listaCartas])):
			if countJogadores == len(jogadores):
				break
			cartasRodada.append(cartas[listaCartas][i])
			countJogadores += 1
			i += 1 
		
		while(countJogadores < len(jogadores)):
			if listaCartas == 3:
				return jogadores
			
			i = 0
			listaCartas += 1
			while(i < len(cartas[listaCartas])):
				if countJogadores == len(jogadores):
					break
				
				cartasRodada.append(cartas[listaCartas][i])
				countJogadores += 1
				i += 1 
				
		resultado = avaliaRodada(jogadores, cartasRodada)
		
		if len(resultado) > 0:
			return resultado
		
numJogadores = int(input())

while(numJogadores != 0):
	jogadores = input().split()
	cartas = []
	for i in range(4):
		entradaCartas = input().split()
		transformaInt(entradaCartas)
		cartas.append(entradaCartas)
	
	vencedores = jogo(jogadores, cartas)
	for jogador in vencedores:
		print("%s " %jogador),
	
	print()
	numJogadores = int(input())
