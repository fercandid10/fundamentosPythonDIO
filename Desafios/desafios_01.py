
'''
#01

numero = int(input())

print(f'{"Par" if numero % 2 == 0 else "Impar"}')
'''
'''
#02
def verificador_ano_bissexto():
    ano = int(input())
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NAO")
        



verificador_ano_bissexto()    
'''

#03

def conta_vogais(texto):
    vogais = ("aeiouAEIOU")
    contador = 0
    for letra in texto:
        for char in vogais:
            if letra == char:
                contador += 1


    return contador 

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto} é: {resultado}")




