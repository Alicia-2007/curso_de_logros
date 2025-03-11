
# Online Python - IDE, Editor, Compiler, Interpreter
#actividad hogar

#ejercicio 1 
#¿Puedes escribir un programa que tome la edad de una persona como entrada y determine si es mayor de edad?
numero= int(input('ingresar numero: '))
rango= 18
resultado= numero>rango
print (resultado)

#Ejercicio 2: Par o impar
#¿Puedes escribir un programa que tome un número como entrada y determine si ese número es par o impar?
numero= int(input('ingresar numero: '))
resultado= numero%2==0
print (resultado)

#Ejercicio 3: Comparar dos números
#¿Puedes escribir un programa que tome dos números como entrada y determine si los dos números son iguales?
a= int(input('ingresar primer numero: '))
b= int(input('ingresar segundo numero: '))
resultado= a==b
print (resultado)

#Ejercicio 4: Verificar si el año es bisiesto
#¿Puedes escribir un programa que tome un año como entrada y determine si ese año es bisiesto?
numero= int(input('ingresar cantidad de dias en ese año: '))
rango= 366
resultado= numero==rango
print (resultado)

#Ejercicio 5: Calcular el descuento en una compra
#¿Puedes escribir un programa que tome el precio de un producto y el porcentaje de descuento como entrada, y calcule el precio final con el descuento aplicado? Además, ¿puedes determinar si el precio final es menor a 100?
precio= int(input('ingresar precio del producto: '))
descuento= int(input('ingresar descuento del producto: '))
resultado_monto_descuento=precio*(descuento/100) 
precio_final= precio-resultado_monto_descuento
print(f' el precio final es:{precio_final}')
print(f' ¿el precio final es menor a 100?')
rango= 100
resultado= precio_final<rango
print(f' La respuesta es:{resultado}')






