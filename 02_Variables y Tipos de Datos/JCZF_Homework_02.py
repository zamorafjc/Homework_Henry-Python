# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
from cmath import pi


Var_1 = 8
print(Var_1)

# 2 Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3. Imprimir el tipo de dato de la variable creada en el punto 1
print(type(Var_1))

# 4. Crear una variable que contenga tu nombre
var_2 = 'Juan Carlos'

# 5. Crear una variable que contenga un número complejo
var_3 = 4+2j

# 6. Mostrar el tipo de dato de la variable creada en el punto 5
print (type(var_3))

# 7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
var7 = pi
print (round(var7,4))

# 8. Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var8= 'True'
var81 = True
### No es lo mismo uno es un valor de cadena y el otro es un valor Bool
# 9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(var8))
print(type(var81))

# 10. Asignar a una variable, la suma de un número entero y otro decimal
var10 = 7 + 4.3
print(var10)

# 11 Realizar una operación de suma de números complejos
print(4+6j + 2+2j)

# 12. Realizar una operación de suma de un número real y otro complejo
print(120+(6+3j))

# 13.Realizar una operación de multiplicación
print(5*9)

# 14. Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

# 15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
var15 = 27
var151 = 4
var152 = var15/var151
print(var152)

# 16. De la división anterior solamente mostrar la parte entera
print(int(var152))

# 17. De la división de 27 entre 4 mostrar solamente el resto
var17=var15%var151
print (var17)

# 18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4*int(var152)+(var17))

# 19. Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var191 = 'Juan Carlos'
var192 = ' Zamora'
var192 = var191 + var192
print (var192)

# 20. Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
var201 = '2'
var202 = 2
print (var201 == var202)
#### No son iguales el resultado es False

# 21. Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
var201 = '2'
var202 = 2
print (var201 == str(var202))

# 22. ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
### bota error porque el texto a convertir a flotante es 3,8 y Python no reconoce la coma como signo decmal debe er el punto a=float('3.8')

# 23. Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var23=3
print(var23)
var23-=3
print(var23)

# 24. Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(bin(1))
print (1<<2)
print (bin(1<<2))
'Da 4 porque se esta trabajando con numeros binarios que son representaciones de ceros y unos. En este caso el binario de 1 es 0001, pero si desplazamos dos unidades a la izquiera, se tiene el numero binario 0100 cuyo valor decimal es 4'

# 25. Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
## print (2 + '2') 'TypeError: unsupported operand type(s) for +: 'int' and 'str''
var251 = 2
var252 = '2'
print(var251 + int(var252))
print(str(var251) + var252)
## en un caso da 4 y en otro '22'

# 26. Realizar una operación válida entre valores de tipo entero y string
var261 = 5
var262 = 'manolo'
print(var261 * var262)
