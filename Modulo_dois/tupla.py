
frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])

matriz = ((1, "a", 2),
          ("b", 3, 4),
          (6, 5, "c"),)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

cores = ("vermelho", "azul", "verde", "azul",)
cores.count("vermelho")
cores.count("azul")
cores.count("verde")

linguagens = ("python", "js", "c", "java", "csharp",)
linguagens.index("java")
linguagens.index("python")
print(len(linguagens))

car = ("gol")
print(isinstance(car, tuple))