num1=int(input("digite o primeiro número: "))
num2=int(input("digite o segundo número: "))
num3=int(input("digite o terceiro número: "))
maior = num1
print("1º Número: ", num1, " 2º Número: ", num2, " 3º Número", num3)

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print("Maior", maior)