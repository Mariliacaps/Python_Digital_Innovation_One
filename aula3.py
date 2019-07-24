a = int(input("Primeiro bimestre: "))
# if que valida e da error na hora em que a variavel nao é digitada corretamente
if a > 10:
    a = int(input("Você digitou errado. Primeiro Bimestre: "))
b = int(input("Segundo bimestre: "))
if b > 10:
    b = int(input("Você digitou errado. Segundo Bimestre: "))
c = int(input("Terceiro bimestre: "))
if c > 10:
    c = int(input("Você digitou errado. Terceiro Bimestre: "))
d = int(input("Quarto bimestre: "))
if d > 10:
    d = int(input("Você digitou errado. Quarto Bimestre: "))
media = (a + b + c + d) / 4
print("Média: {}".format(media))

# esse if nao deixa digitar nenhuma nota acima de 10 para nao ocorrer error
# if a <= 10 and b < 10 and c < 10 and d < 10:
#     print("Media: {}".format(media))
# else:
#     print("Foi informada uma nota errada")



# a = int(input("Entre com um valor: "))
# b = int(input("Entre com um segundo valor: "))
# resto_a = a % 2
# resto_b = b % 2
# # usado quando uma das entradas é verdadeira
# # if resto_a == 0 or resto_b == 0:
# # o not inverte o valor
# if resto_a == 0 or not resto_b > 0:
#     print("foi digitado um número par")
# else:
#     print("nenhum número é par")



# a = int(input("Primeiro valor: "))
#  b = int(input("Segundo valor: "))
#  c = int(input("Terceiro valor: "))
#  if a > b and a > c:
#      print("o maior número é {}".format(a))
#  elif b > a and b > c:
#      print("O maior número é {}".format(b))
#  else:
#      print("O maior número é: {}".format(c))
#  print("final do programa")
