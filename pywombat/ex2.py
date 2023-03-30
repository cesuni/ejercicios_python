''' 
Elementos que mas se repiten 
'''

while True:
    number = input('Guess the number: ')

    try:
        number = int(number)
    except:
        print('Sorry that is not a number')
        continue
