# lista
# a lista sempre tem que ter colchetes "[]"
# a lista aceita numero e strings ...
# para inprimir apenas um item da lista colocar a variavel e o numero correspondente entre "[]"
lista = [12, 10, 5, 7]
lista_animais = ["cachorro", "gato", "elefante", "lobo", "arara"]

#tupla é imutavel(não pode ser alterada) e lista é mutavel(pode ser alterada)
tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))# comando len conta quantos elementos tem na lista
tupla_animal = tuple(lista_animais)#comando "tuple" converte a lista em tupla
print(type(tupla_animal))# diz a classe
print(tupla_animal)

#essa conversão serve pra alterações em tupla
lista_numerica = list(tupla)# o comando "list" converte a tupla em lista
print(type(lista_numerica))# mostra a classe
print(lista_numerica)

# # comando ".sort()" ele vai ordenar as listas, por ordem alfabetica e por numeros do maior pro menor
# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# # para reverter a ordenação
# lista_animais.reverse()
# print(lista_animais)

# print(lista_animais[0])
#
# # esse método é para somar todos os numeros da lista
# # soma = 0
# # for x in lista:
# #     print(x)
# #     soma += x
# # print(soma)
#
#
# print(sum(lista))
# # metodo simplificado de somar numeros de uma lista (funciona somente com numero)
#
# print(max(lista))
# # procura o maior numero da lista
#
# print(min(lista))
# # imprime o menor valor da lista (pode ser usado com string)
#
# #if usado para ver se consta uma certa string na lista
# if "lobo" in lista_animais:
#     print("Existe um lobo na lista")
# else:
#     print("Não existe um lobo na lista")
#     # incluir um animal que nao esta na lista
#     lista_animais.append('lobo')
#     print(lista_animais)
#
# # retirar item da lista
# lista_animais.pop(0) #pode-se escolher a localização colocando o numero entra "()"
# print(lista_animais)
#
# #usado para remover um item que eu ja conheço da lista
# lista_animais.remove("elefante")
# print(lista_animais)



# # criar uma nova lista
# nova_lista = lista_animais * 3
# print(nova_lista)
