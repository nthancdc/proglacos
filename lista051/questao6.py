'''
6)	Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
'''

n = int(input("Me diga um número entre 1 e 50: "))

if (n <= 50):
    while (n * 3 <= 250):
        mult = n * 3
        print(f"A multiplicação de {n} por 3 é: {mult}")
        n = n + 1
else:
    print("O seu número não está entre 1 e 50.")