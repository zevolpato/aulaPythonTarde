"""
nome = "Jose"
numero = 6
troco = 4.65
is_login = True # sempre com a primeira letra maiuscula True
print(type(nome))
print(type(numero))
print(type(troco))
print(type(is_login))
"""
nomes = [ "Maria", "João", "Fábio", "Ana", "Zé" ]
print(type(nomes)) #mostrar o tipo List
print(nomes) #mostra a lista
# print(nomes[1]) # mostra a posição 2
print(nomes.pop()) # exclui a ultima posição e mostra o nome excluido
print(nomes) # mostrar a lista novamente
nomes.pop() # exclui a ultima posicao
print(nomes)
nomes.append("Ana") #adiciona um nome no final da lista
nomes.append("Lorenzo") 
print(nomes)

for x in nomes:
    print(x)

#ensinar escopo
