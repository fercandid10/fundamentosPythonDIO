class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __delete__(self):
        print("Removendo a instancia da classe.")

    def falar(self):
        print("Latiu..auau")


c1 = Cachorro("Chappie", "amarelo")
c1.falar()