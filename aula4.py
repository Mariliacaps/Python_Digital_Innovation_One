# for x in range(1, 200):
# # posso escolher o numero de inicio
#     print (x)
# # vai imprimir os 100 primeiros numeros até 100


# # aqui vai descobrir os números primos
# a = int(input("entre com um número: "))
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#         #div = div +1
# if div == 2:
#     print("Número {} é primo".format(a))
# else:
#     print("Número {} não é primo".format(a))

# # aqui vai imprimir todos os numeros primos de 0 até 100 (101)
# # o input limita até onde saber os numeros primos
# a = int(input("Entre com um número: "))
# for num in range(a+1):
#     div = 0
#     # abaixo o for x vai percorrer os numeros dentro de 101
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#         # += equivale a div = div + 1
#             div += 1
#     if div == 2:
#             print(num)

# # laço de repetição while
# # diferente do for ele precisa de variavel
# a = 0
# while a <= 10:
#     print (a)
#     a += 1

# # AULA3 usando o while
# nota = int(input("Entre com a nota: "))
# while nota > 10:
#     # sempre que digitar uma nota maior que 10 o programa vai pedir novamente a nota correta.
#     nota = int(input("Entre novamente com a nota: "))
# print(nota)

a = int(input("Primeiro bimestre: "))
# o while força o usuario a digitar corretamente
while a > 10:
    a = int(input("Você digitou errado. Primeiro Bimestre: "))
b = int(input("Segundo bimestre: "))
while b > 10:
    b = int(input("Você digitou errado. Segundo Bimestre: "))
c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input("Você digitou errado. Terceiro Bimestre: "))
d = int(input("Quarto bimestre: "))
while d > 10:
    d = int(input("Você digitou errado. Quarto Bimestre: "))
media = (a + b + c + d) / 4
print("Média: {}".format(media))
