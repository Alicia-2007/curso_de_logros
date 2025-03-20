
# Online Python - IDE, Editor, Compiler, Interpreter
 #practica 3 clase 2
  #ejercicio 1
a = int(input('Ingrese 1er numero: '))
b = int(input('Ingrese 2do numero '))
print(f'¿ambos numeros son positivos?')
funcion_and= a>0 and b>0 
print(funcion_and)
print(f'¿al menos uno de los dos numeros es positivo?')
funcion_or= a>0 or b>0 
print(funcion_or)
print(f'¿el primer numero no es negativo?')
funcion_not= not a<0 
print(funcion_not)

 #ejercicio 2
edad = int(input('Ingrese edad: '))
print(f'¿estas entre 18 y 64?')
rango= edad<=64 and edad>=18
print(rango)
print(f'¿eres menor de edad?')
menor= not edad>18
print(menor) 
