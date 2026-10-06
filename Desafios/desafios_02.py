'''
#01
def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()

    elementos = tuple(map(int, entrada.split()))

    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
'''
# Reveja string, split e map

'''
#02
def elementos_comuns(lista1, lista2):

    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return sorted(list(set1.intersection(set2)))

lista1 = input().split()
lista2 = input().split()

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns as duas listas: {comuns}")
else:
    print("Entrada invalida.")

'''

#03
def contar_caracteres(string):
    contador = {}

    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

    return contador

entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)











