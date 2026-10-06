'''
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)

print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)
'''

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento


    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Fer", 1998)

print(f"Nome: {pessoa.nome} \Idade: {pessoa.idade}")