import math

a = None
b = None
try:
    entrada = input('Ingrese los números que desea ingresar: ')
    numeros= entrada.split()

    if len(numeros) == 2:
        a, b = map(float, numeros)
    elif len(numeros) == 1:
        a = float(numeros[0])
        b = None
    else:
        print('Debe ingresar uno o dos números unicamente') 
    signo = input('Indique que opeación desea realizar: ')
except ValueError:
    print('Parámetro o valor desconocido')

x = math.radians(a)

if signo == '+'and b is not None:
    print(a + b) 
elif signo == '-'and b is not None:
    print(a - b) 
elif signo == '*'and b is not None:
    print(a * b) 
elif signo == '/'and b is not None:
    print(a / b) 
elif signo == '**'and b is not None:
    print(a**b) 
elif signo == '%'and b is not None:
    print(a%b) 
elif signo == 'sin' and a is not None:
    print(math.sin(x)) 
elif signo == 'raiz cuadrada' and a is not None :
    print(math.sqrt(a)) 
elif signo == 'cos' and a is not None:
    print(math.cos(x))
elif signo == 'tan' and a is not None:
    print(math.tan(x))

    