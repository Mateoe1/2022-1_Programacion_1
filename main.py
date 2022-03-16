from math import sqrt
import os
import msvcrt

def lista_org():
    frase_num = input("Añada tantos numeros como quiera separados por ',': ")
    list_num = frase_num.split(',')
    list_new = []
    for numero in list_num:
        list_new.append(int(numero))

    list_new.sort(reverse = True)
    print(list_new)

def operaciones():
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))

    print('')
    print(f'Suma {x} + {y} es: {x + y}')
    print(f'Resta {x} - {y} es: {x - y}')
    print(f'Multiplicacion {x} * {y} es: {x * y}')
    print(f'Division {x} / {y} es: {x / y}')

def fibonacci():
    n = int(input("Ingrese un numero: "))
    seq = []
    for i in range(1, n):
        fib = int(((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))) #ecuacion para saber un numero dentro de la serie ubicado en n

        if fib < n :
            seq.append(fib)

    print(' ')
    print(f'Lista de los numeros dentro de secuencia de Fibonacci menores a {n}: ')
    print(*seq)

def conteo_caracteres():
    list_cont = []
    frase = input("Ingrese una frase: ")
    frase = frase.split()
    frase = ''.join(frase)
    print(' ')
    dic = {}

    for letra in frase:
        try:
            dic[letra] += 1
        except KeyError:
            dic[letra] = 1

    list_el = list(dic.items())
    list_el.sort(key = lambda a: a[1], reverse = True)

    for item in list_el:
        if item[1] == 1:
            print(f"la {item[0]} esta {item[1]} vez")
        else:
            print(f"La {item[0]} esta {item[1]} veces")

def limpiar():

    print("Presione enter para limpiar y volver al menú")
    enter = str(msvcrt.getch(),'utf -8') #Lee una pulsacion de tecla
    if enter == "\r": #\r corresponde a enter
        os.system('cls') #limpia la ventana de comandos


if __name__ == '__main__':
    opcion = '1'
    while opcion != '0':
        print("Ingrese el numero de la opcion a ejecutar: ")
        print("1. Organizacion de mayor a menor de una lista de numeros")
        print("2. Operaciones de 2 numeros")
        print("3. Serie de fibonacci menor a numero ingresado")
        print("4. Conteo de caracteres de una frase")
        print("0. Salir")
        opcion = input()
        print('')
        os.system('cls')

        if opcion == '1':
            print("1. Organizacion de mayor a menor de una lista de numeros")
            print('')
            lista_org()
        elif opcion == '2':
            print("2. Operaciones de 2 numeros")
            print('')
            operaciones()
        elif opcion == '3':
            print("3. Serie de fibonacci menor a numero ingresado")
            print('')
            fibonacci()
        elif opcion == '4':
            print("4. Conteo de caracteres de una frase")
            print('')
            conteo_caracteres()
        elif opcion == '0':
            print("Ha salido del programa")
            break;
        else:
            print("Opcion no encontrada")
        print('')

        
        limpiar()
