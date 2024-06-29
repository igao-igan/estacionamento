clientes = []


def estacionamento(n1, ndc):
    if n1 >= 1:
        
        clientes.append(ndc)
        
        if ndc == 1:
            
            return len(clientes)
    return None  


n1 = int(input('Número do carro: '))
ndc = int(input('Número do cliente: '))


r = estacionamento(n1, ndc)

if r is not None:
    print(f"Número máximo de clientes que podem estacionar: {resultado}")
else:
    print("Cliente não é o primeiro, não afeta o estacionamento.")