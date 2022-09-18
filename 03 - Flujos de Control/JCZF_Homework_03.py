### Flujos de control

# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
var1 = 0
if var1 > 0:
    print (var1,'es mayor que 0')
elif (var1 < 0):
    print(var1,'es menor que 0')
else: 
    print(var1,'es igual a 0')

# 2. Crear dos variables y un condicional que informe si son del mismo tipo de dato
var21 = 76
var22 = 86.25
if type(var21) == type(var22):
    print (var21,' y ',var22,'Si son del mismo tipo de dato')
else:
    print (var21, 'y', var22,'No son del mismo tipo de dato')

# 3. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
var31=1
var32=21
for var31 in range(var31,var32):
    if var31%2 == 0:
        print(var31,'Es un numero par')
    else:
        print(var31,'No es un numero par')

# 4. En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
var41 = 0
var42 = 5
for var41 in range(var41,var42+1):
    print(var41, 'elevado a la potencia 3 es igual a ', var41**3)

# 5. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
var51= 3
for var51 in range(0,var51):
    print('ciclo ', var51)

# 6. Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
var61 = 5
var62 = var61 - 1
var_fac = var61
if var62 > 0:
    if type(var62) == int:
        while var62 > 0:
            var_fac = var_fac * var62
            var62 = var62 - 1
        print(var_fac,'es el factorial de',var61)
    else:
        print(var62, 'No es entero')
else:
    print(var62, 'No es mayor de 0')

# 7. Crear un ciclo for dentro de un ciclo while
var71 = 7
var73 = var71
print('Los factoriales de los numeros menores a ', var71)
while var73 > 0:
    factor=1    
    for x in range(1,(var71+1)):
        factor = factor * x
    print('El factorial de: ', var71, 'es :', factor)
    var73 = var73 - 1
    var71 = var71 - 1
print('Los factoriales')

# 8. Crear un ciclo while dentro de un ciclo for
var81 = 3
print('la tabla de multiplicar del 1 al', var81)
while var81>0:
    var8=var81
    for x in range(1,10):
        print (var8,'*',x,'=',var8*x)
    print('la tabla del:',var8)
    var81 = var81 -1

# 9. Imprimir los números primos existentes entre 0 y 30
var93 = 2
var94 = 30
print('Los numeros primos entre ', 0 , 'y', var94)
while var93 <= var94:
    var92 = 1
    for x in range(2,var93):
        if (var93%x) == 0:
            var92 = 0
    if var92 == 1:
         print(var93)
    var93 = var93 + 1

# 10. Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
var93 = 2
var94 = 100
print('Los numeros primos entre ', 0 , 'y', var94)
while True:
    if var93 == var94:
        break
    var92 = 1
    for x in range(2,var93):
        if (var93%x) == 0:
            var92 = 0
    if var92 == 1:
         print(var93)
    var93 = var93 + 1

# 11. En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?


# 12. Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
var131 = 100
var132 = 300
print('Los numeros divisibles por 12 entre', var131, 'y', var132)
while True:
    if var131 == var132:
        break
    if var131%12 == 0:
        print(var131)
    var131 = var131 + 1

# 14. Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
while True:
    var141 = int(input('Ingrese el numero a validar :' ))
    var143 = 1
    for x in range(2,var141):
        if (var141%x) == 0:
            var143 = 0
    if var143 == 1:
         print(var141, 'Si es un numero primo')
    elif (var143 == 0 ):
        print(var141, 'No es un numero primo')
    var144 = input('Desea continuar? S/N:')
    if var144 == 'N':
        print('Gracias')
        break

# 15. Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
var151 = 100
var152 = 300
var152 = 0
while True:
    if var152 == 1:
        break
    if var151%3 == 0:
        if var151%6 == 0:
            print('El numero: ', var151, 'es divisible por 3 y por 6')
            var152 = 1
    var151 = var151 + 1

