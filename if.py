
'''weather_dry  = False
weather_rain = False'''

'''if weather_dry == False:
    print('Today')
else:
    print('not today') '''


'''if weather_dry == True:
    if weather_rain == False:
        print('Yes')
    else:
        print('not')    
else:
    print('not')'''

n1 = int (input('Ingrese un numero: '))
n2 = int (input('Ingrese un numero: ')) 

'''if n1 == n2:
    print('los valores son iguales')
else:
    if n1 > n2:
        print('El primer numero es mayor')   
    else:
        print('El segundo numero es el mayor')'''


larger_number = max(n1, n2)

print('El numero mas grande es: ', larger_number)
