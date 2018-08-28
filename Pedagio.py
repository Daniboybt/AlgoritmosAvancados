distancias = input().split()

rodovia = int(distancias[0])
pedagios = int(distancias[1])

custos = input().split()

kilometro = int(custos[0])
custoPedagio = int(custos[1])

print ((kilometro * rodovia) + ((rodovia // pedagios) * custoPedagio))
