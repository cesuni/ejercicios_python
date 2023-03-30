''' 
indice de masa corporal 
'''

ps = float(input('Ingrese su peso: '))
al = float(input('Ingrese su altura: '))

'''indice de masa corporal'''
imc = ps / (al**2)

print('su indice de masa corporal es:', imc)

if imc < 18.5:
    print('peso bajo')
else:
    if imc > 25:
        print('peso superior')
if imc < 25:
    print('peso normal')
