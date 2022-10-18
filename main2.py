
#
# Ejercicio 1: Utilice las funciones anteriores para agregar elementos faltantes
# Ejercicio 2: Utilice las funciones anteriores para elminar elementos sobrantes


lista=["P", "t"]
 # TODO
lista.insert(1,"y")
lista.extend(["h","o","n"])
  
print(lista)
assert ''.join(lista) == "Python"
print







def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
  
    # TODO
    assert lista == list(range(1, 6))
    return lista