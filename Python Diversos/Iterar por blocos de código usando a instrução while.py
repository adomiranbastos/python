import random # função de numeros randonicos "aleatorios"

rolar = 0
contar = 0

while rolar != 5: #enquanto o rolar tiver valor diferente de 5 continue a função 
  contar = contar + 1 #contar + 1 porque começa no zero a númeração
  rolar = random.randint(1, 5) #escolher numero aleatorio de 1 a 5
  print(rolar)

print(f'Demorou {contar} rodas para chegar a 5!')