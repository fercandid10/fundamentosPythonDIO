'''
frutas = ["laranja", "maca", "uva"]

#frutas = []

letras = list("Python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

print(frutas[-1])
print(frutas[-2])
print()

matriz = [[1, "a", 2],
          ["b", 3, 4],
          [6, 5, "c"]]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["p", "y", "t", "h", "o","n"]
print()
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
print()
carros = ["gol", "celta", "Palio"]

for carro in carros:
    print(carro)
print()

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

numbers = [1, 30, 21, 2, 9, 65, 34]
pars = [numbers for number in numbers if number % 2 == 0]

n1 = [1, 30, 21, 2, 9, 65, 34]
quadrado = [n ** 2 for n in n1]

'''
#copy()
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)
print(id(l2), id(lista))
print()

#count()
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho")
cores.count("azul")
cores.count("verde")

print()

linguagens = ["python", "js", "c"]
print(linguagens)

linguagens.extend(["java", "c#"])

print(linguagens)

print(linguagens.index("java"))
print(linguagens.index("python"))

linguagens.pop()
linguagens.pop()
linguagens.pop(0)
print(linguagens)

print(linguagens.remove("c"))

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.reverse())
print(linguagens.sort())
print(linguagens.sort(reverse=True))
print(linguagens.sort(key=lambda x: len(x))) 
print(linguagens.sort(key=lambda x: len(x), reverse=True))

print(len(linguagens))


print([n ** 2 if n > 6 else n for n in range(10) if n % 2 == 0])

