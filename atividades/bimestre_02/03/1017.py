tempo = int(input('Tempo da viagem: '))
velocidade_media = int(input('Velocidade média: '))

distancia = tempo * velocidade_media

# o carro tem autonomia de 12km por litro
litros = distancia/12

print(f'{litros:.3f}')