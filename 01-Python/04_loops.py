# Bucle con rangos de iteracion definidos
for x in range(0, 5):
    print(f"Numero de iteracion: {x}")

for x in range(3):
    print(f"Numero de iteracion {x}")

for x in range(3, 10):
    print(f"Numero de iteracion {x}")

for indice in range(7, 10):
    print(f"Numero de iteracion {indice}")

for indice in range(10):
    if indice == 6:
        break  # Detener la ejecucion del loop
    print(f"Numero de iteracion {indice}")


for indice in range(10):
    if indice == 6:
        continue  # Detener la ejecucion de esta iteracion, el loop continua
    print(f"Numero de iteracion {indice}")

numeroAuxiliar = 0

while numeroAuxiliar < 10:
    print(f"Numero {numeroAuxiliar}")
    numeroAuxiliar += 1

numeroAuxiliarDos = 0
while True:
    print(f"Numero {numeroAuxiliarDos}")
    numeroAuxiliarDos += 1
    if numeroAuxiliarDos == 70:
        break
