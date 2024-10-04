n = int(input("Introduzca un número igual o mayor a 1: "))
for num in range(1, n +1):
    if num % 3 == 0 and num % 5 == 0:
        print('FooBar')
    
    elif num % 3 == 0:
        print('Foo')
        
    elif num % 5 == 0:
        print('Bar')

    else:
        print('El número ' + str(num) + ' no es divisible ni por 3 ni por 5.')