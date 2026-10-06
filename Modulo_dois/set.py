print(set([1, 2, 3, 1, 3, 4]))
print(set("abacaxi"))
print(set(("palio", "gol", "celta", "palio")))

print()
linguagens = {"python", "java", "python"}
print(linguagens)

print()
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

print()
conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))
print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))

print()
conj_a = {1, 2, 3, 4, 5}
conj_b = {6, 7, 8, 9}
conj_c = {1, 0}

print(conj_a.isdisjoint(conj_b))
print(conj_a.isdisjoint(conj_c))

print()
sorteio = {1, 23}

print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(25))
print(sorteio.copy())

print(sorteio.clear())

print()

nums = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(nums)
print(nums.discard)
print(nums.discard(45))
print(nums)
print(nums.pop())
print(nums)

print(nums.remove(0))
print(len(nums))
print(1 in nums)
print(10 in nums)
