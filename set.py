lista = ("tarefa1", "tarefa2", "tarefa3")
print(lista) # mostrar lista
print(type(lista)) # mostrar tipo da lista -> tuple
x = list(lista)
print(type(x))
x.append("tarefa4")
lista = tuple(x)
print(lista) 
print(type(lista))


         