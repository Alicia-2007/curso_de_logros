
# Online Python - IDE, Editor, Compiler, Interpreter
 #practica 2 clase 2
  #ejercicio 1
a = int(input('Ingrese 1er numero: '))
b = int(input('Ingrese 2do numero '))
print(f'¿uno de los numeros es mayor?')
mayor= a>b 
print(mayor)
print(f'¿uno de los numeros es menor?')
menor= a<b 
print(menor)
print(f'¿son iguales?')
igual= a==b 
print(igual)

  #ejercicio 2
a = int(input('Ingrese 1er numero: '))
b = int(input('Ingrese 2do numero ')) 
c = int(input('Ingrese 3er numero '))
print(f'¿el primer numero es mayor?')
a_b= a>b 
print(a_b)
print(f'¿uno de los dos primeros numeros es menor?')
b_a= b>a
print(b_a)
print(f'¿el tercer numero es mayor a los otros dos?')
c= c>a_b
print(c)