a=10
b=5
soma= a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
resto= a%b
print("Soma: " + str(soma))
# o melhor jeito é usar o format
# print("Subtração: " +str(subtracao))
# ou print("Subtração: {}" .format(subtracao))
# O \n EQUIVALE AO ESPAÇO NA COMPLIAÇÃO DO CÓDIGO
print(f"Subtração: {subtracao}")
print("Multiplicação: " +str(multiplicacao))
print(int(divisao))
print("Resto: "+str(resto))
# mini exemplo de como usar string em uma equação
# x='1'
# soma2=int(x)+1
# print(soma2)