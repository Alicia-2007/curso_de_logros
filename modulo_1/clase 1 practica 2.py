#práctica 2
#ejercicio 1
a= int(input('ingresa primer numero: '))
b= int(input('ingresa segundo numero: '))
suma= a+b
print(f' La suma de los numeros es {suma}')
resta= a-b 
print(f' La resta de los numeros es {resta}')
multiplicacion= a*b
print(f' La multiplicacion de los numeros es {multiplicacion}')
division= a/b
print(f' La division de los numeros es {division}')

#ejercicio 2
numero= int(input('ingresar numero: '))
a= "par"
b= "impar" 
if(numero %2)==0:
    print (f' el numero es {a}')
else:
    print(f' el numero es {b}')

#ejercicio 3
numero= int(input('ingresar numero: '))
a= "esta en el rango"
b= "no esta en el rango"
if (numero >10 and numero <20):
    print (f' el numero es {a}')
else:
    print(f' el numero es {b}')
