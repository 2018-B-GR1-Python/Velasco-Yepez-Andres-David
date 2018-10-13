tupla = (1, 2, 3, 4, 5, 6, "a", "a", "a")
print(tupla.index(2))  # Devuelve el indice
print(tupla.count(1))  # Devuelve el numero de repeticiones del valor
print(tupla[0])  # 3
print(tupla[0:2])

print(set(tupla))  # Tupla sin repetiddos

# Iterar tupla sin repetidos
for t in set(tupla):
    print(f"Valor: {t}")

arregloUno = [1, 2, 3]
arregloDos = [4, 5, 6]
