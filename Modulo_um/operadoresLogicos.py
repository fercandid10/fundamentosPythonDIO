saldo = 1000  
saque = 250
limite = 200
contaEspecial = True



#print(True and True) # 1 * 1 = 1
#print(False and False) # 0 * 0 = 0
#print(False and True) # 0 * 1 = 0
#print(True or False) # 1 + 0 = 1
#print(False or False) # 0 + 0 = 0
#print(True or True) # 1 + 1 = 2

exp = (saldo >= saque and saque <= limite) or (contaEspecial and saldo >= saque)
print(exp)