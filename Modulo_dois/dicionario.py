'''
pessoa = {"nome": "Fernando", "idade": 28}

pessoa1 = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234"

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])
print()

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "guivanna@gmail.com": {"nome" : "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}}, 
}

print(contatos["guivanna@gmail.com"]["telefone"])

extra = contatos["melaine@gmail.com"]["extra"]
print(extra)
print(extra["a"])
print()

for chave in contatos:
    print(chave, contatos[chave])

print()

for chave, valor in contatos.items():
    print(chave, valor)
'''

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": 3333-2221}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])
print(copia["guilherme@gmail.com"])

print()
print(contatos.get("guilherme@gmail.com"), {})
print()
print(contatos.keys())
print()
print(contatos.pop("guilherme@gmail.com", "Nao encontrou!"))
print()

p1 = {"nome": "Fer", "tel": "9999-1234"}

p1.setdefault("nome", "Nando")
print(p1)

p1.setdefault("idade", 28)
print(p1)
print()

p2 = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

p2.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(p2)

p2.update({"giovanna@gmail.com": {"nome": "Giovana", "telefone": "3332-8811"}})
print(p2)
print()
print(p2.values())
print()

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "guivanna@gmail.com": {"nome" : "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}}, 
}

print("guilherme@gmail.com" in contatos)
print("theflash@gmail.com" in contatos)
print("telefone" in contatos["chappie@gmail.com"])

print()
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos)

