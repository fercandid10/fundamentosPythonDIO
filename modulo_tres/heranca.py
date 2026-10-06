class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"Cor {self.cor}, Placa {self.placa}, Rodas {self.num_rodas}"


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "ABC-1234", 2)
#moto.ligar_motor()

carro = Carro("branca", "CDW-4321", 4)
#carro.ligar_motor()

caminhao = Caminhao("Verde", "RTW-6789", 8, True)
#caminhao.ligar_motor()

print(moto)
print(carro)
print(caminhao)
