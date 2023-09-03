'''
#Primer Archivo De Python
print('hello world') #Primer Ejercicio
mundo= 'hello world'
print(mundo);      #Segundo  Ejercicio;


#Tercer Ejercicio
nombre= input('¿Cómo te llamas? ')
print('Tu nombre es ' + nombre + '?');

#Ejercicio 4
print(((3+2)/(2*5))**2);

#Ejercicio5
ht=float(input('escribe las horas trabajadas: '));
ch=float(input('escribe el costo por hora: '));
pago= str(ht*ch);
print('A usted le deben '+ pago);

#Ejercicio 6
N=int(input('escribe un numero entero positivo '))
print(N*(N+1)/2)

#Ejercicio 7
peso= float(input("Introduzca su peso en kg aqui: "))
estatura= float(input("Introduzca su estatura en metros aqui: "))
imc=round(peso/estatura**2,2)
print("Tu ìndice de masa corporal es ",imc)


#Ejercicio 8
N= int(input("Introduzca un número entero: "))
M= int(input("Introduzca un número entero: "))
D= N/M
C= N//M
R= N%M
print("El resultado de la division es:",D,", El residuo es:",R,", su cociente es:",C)

#Ejercicio 9
inversion=float(input("Cantidad a invertir: "))
IA=float(input("El interes anual es: "))
años=float(input("El numero de años invertido es: "))
formula= inversion*(IA/100+1)**años
print("El capital obtenido es: ",formula)

#Ejercicio 10
PP=int(input("Cuantos payasos quieres pedir: "))
PM=int(input("Cuantas muñecas quieres pedir: "))
formula= (PP*112)+(PM*75)
print("El peso total del paquete es",formula,"g")

#Ejercicio 11
def calcular_ahorros(cantidad_inicial, años, tasa_interes):
    saldo = cantidad_inicial
    for _ in range(años):
        saldo += saldo * (tasa_interes / 100)
    return saldo

cantidad_inicial = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))
tasa_interes = 4  # 4% de interés anual
años = [1, 2, 3]

for año in años:
    ahorros = calcular_ahorros(cantidad_inicial, año, tasa_interes)
    print(f"Después de {año} años, tendrás ${round(ahorros, 2)} en tu cuenta de ahorros.")

#Ejercicio 12
precio_pan = 3000
descuento = 0.4 

panes_no_frescos = int(input("Ingrese el número de panes no frescos vendidos: "))

precio_habitual = precio_pan
descuento_aplicado = precio_pan * descuento
costo_final = precio_pan - descuento_aplicado

print(f"Precio habitual de un pan: ${precio_habitual}")
print(f"Descuento por no ser fresco: ${descuento_aplicado:.2f}")
print(f"Costo final total: ${costo_final:.2f}")

#Ejercicio 14
n= 0
n= int(input("Ingrese un numero entero positivo: "))

suma=n * (n + 1) / 2
if suma > 20:
  print("La suma de todos los enteros desde 1 hasta " + str(n) + " es " + str(suma) + " es un gran número!")
else:
  print("La suma de todos los enteros hasta desde 1 hasta " + str(n) + " es " + str(suma))

#Ejercicio 15
n= 0
m= 0

n= int(input("Introduzca un número entero: "))
m= int(input("Introduzca un número entero: "))
D= n/m
C= n//m
R= n%m

if C < 1:
  print("El resultado de la division es:",D,", El residuo es:",R,", su cociente es:",C, " el divisor es mayor al dividendo.")

if C > 1:
  print("El resultado de la division es:",D,", El residuo es:",R,", su cociente es:",C," el divisor es menor que el dividendo")

if C == 1:
  print("El resultado de la division es:",D,", El residuo es:",R,", su cociente es:",C," el divisor es igual al dividendo")

#ejercicio 15

inversion=float(input("Cantidad a invertir: "))
IA=float(input("El interes anual es: "))
años=float(input("El numero de años invertido es: "))
formula=round(inversion*((IA/100)+1)**años,2)
if inversion < 100000:
  print("El valor de su inversion es:",formula,", baja rentabilidad.")

if inversion > 100000 and inversion < 1000000:
  print("El valor de su inversion es:",formula,", rentabilidad moderada.")

if inversion >= 1000000:
  print("El valor de su inversion es:",formula,", es una buena inversion")

#ejercicio 16
payaso= 0
muñeca= 0
peso_payaso= 112
peso_muñeca= 75
pedido_payaso=int(input("Cuantos payasos quieres pedir: "))
pedido_muñeca=int(input("Cuantas muñecas quieres pedir: "))
payaso_kg= (pedido_payaso*peso_payaso)/1000
muñeca_kg=(pedido_muñeca*peso_muñeca)/1000
peso_total= payaso_kg+muñeca_kg
print(peso_total)

if peso_total > 3000:
  x=input("Desea enviarlo? ")
  if x=="si":
    print("Contenedor enviado")
  if x=="no":
    print("Contenedor no enviado")
  else:
    print("Error en el sistema")
print(peso_total)

#ejercicio 17
ca= 0
i1= 0
i2= 0
i3= 0

ca= float(input(""))

#Ejercicio funciones1
n1=0
n2=0
n1=int(input("Deme un n1: "))
n2=int(input("Deme un n2: "))
def suma(a,b):
  sum=(a+b)
  print("La suma de sus numeros es",sum)


#Ejercicio funciones2
n1=0
n2=0
n1=int(input("Deme un n1: "))
n2=int(input("Deme un n2: "))
def resta(a,b):
  minus=(a-b)
  print("La resta de sus numeros es",minus)


#Ejercicio funciones3
n1=0
n2=0
n1=int(input("Ponga su numero: "))
n2=int(input("Ponga su otro numero: "))
def times(a,b):
  x=(a*b)
  print("La multiplicacion de sus numeroses",x)


#Ejercicio funciones4
n1=0
n2=0
n1=int(input("Ponga numero entero: "))
n2=int(input("Ponga su otro numero entero: "))
def division(a,b):
  if b==0:
    print("No se puede dividir por 0 huevon")
  else:
    divide=(a/b)
    print("La division de sus numeros es",divide)

#Ejercicio funciones5
n1=0
n2=0
n1=int(input("Que numero quiere calculado: "))
n2=int(input("Que numero quiere calculado: "))
def calculadora(a,b):
  P=input("Que quieres hacer con esos dos numeros: ")
  if P=="suma":
    suma(n1,n2)
  elif P=="resta":
    resta(n1,n2)
  elif P=="multiplicacion":
    times(n1,n2)
  elif P=="division":
    division(n1,n2)
  else:
    print("Chupemela soy una calculadora, le pedi algun calculo")
  
calculadora(n1,n2)

#Ejercicio 6
def intereses(int):
  d= int
  if(d>0 and d<1000000):
    return 2
  elif(d>=1000000 and d<2000000):
    return 5
  else:
    return 7

def calBalance(int, inv):
  n= int
  d= inv
  return round((d*(1+(n/100))),2)

def ctaAhorro():
  inversion= float(input("Ingrese el valor de la inversion: "))
  interes=intereses(inversion)
  b1=calBalance(interes, inversion)
  b2=calBalance(interes, b1)
  b3=calBalance(interes, b2)
  print("balance 1: ",b1,"balance 2: ",b2,"balance 3: ",b3)

ctaAhorro()
#Ejercicio 7
def areaT(a,b):
  return(b*a)/2

def areaC1(ac,bc):
  return ac*bc

def areaC2(r):
  return(3,14*(r**2))

def areaP(p,a):
  return(p*a)/2

def areaR(x,y):
  return(x*y)/2
  
def areasFig():
  m= int(input("""Que opcion desea: 
                1:triangulo
                2:cuadrado
                3:circulo
                4:pentagono regular
                5:rombo """))

  if m==1:
    base=float(input("Ingrese su base: "))
    altura=float(input("Ingrese su altura: "))
    Triangulo= areaT(altura, base)
    print("Su area es: ",Triangulo)
  
  elif m==2:
    lado1=float(input("Ingrese el primer lado: "))
    lado2=float(input("Ingrese el segundo lado: "))
    cuadrado=areaC1(lado1, lado2)
    print("Su area es: ",cuadrado)

  elif m==3:
    radio=float(input("Ingrese el radio: "))
    circulo=areaC2(radio)
    print("Su area es: ",circulo)
    
  elif m==4:
    perimetro=float(input("Ingrese el perimetro: "))
    apotema=float(input("Ingrese el apotema: "))
    pentagono=areaP(perimetro, apotema)
    print("Su area es: ",pentagono)

  elif m==5:
    a=float(input("Ingrese el diagonal mayor: "))
    b=float(input("Ingrese diagnoal menor: "))
    rombo=areaR(a,b)
    print("Su area es: ",rombo)
areasFig()

def maximo(a,b):
  if x>y:
    return x
  else:
    return y

def minimo(a,b):
  if x<y:
    return x
  else:
    return y

x=int(input("Numero: "))
y=int(input("Otro numero"))
print(maximo(x-3, minimo(x+2,y-5)))
#MALA PRACTICA VARIABLES GLOBALES

# Función para verificar si un año es bisiesto
def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Función principal del programa
def main():
    # Solicitar al usuario que ingrese un año
    year = int(input("Ingrese un año: "))

    # Llamar a la función es_bisiesto para determinar si el año es bisiesto
    if es_bisiesto(year):
        print(f"{year} es bisiesto")
    else:
        print(f"{year} no es bisiesto")


main()

# Función para determinar el tamaño del perro
def determinar_tamano(altura, peso):
    if altura <= 30:
        if peso <= 15:
            return "Pequeño"
    elif 30 < altura <= 40:
        if 15 <= peso <= 25:
            return "Mediano"
    elif 40 < altura <= 60:
        if 25 <= peso <= 45:
            return "Grande"
    return "Desconocido"

# Función principal del programa
def main():
    # Solicitar altura y peso al usuario
    altura = float(input("Ingrese la altura del perro (en cm): "))
    peso = float(input("Ingrese el peso del perro (en kg): "))

    # Determinar el tamaño del perro utilizando la función
    tamano = determinar_tamano(altura, peso)

    # Mostrar el resultado
    print(f"Tamaño del perro: {tamano}")

main()

# Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir de Celsius a Kelvin
def celsius_a_kelvin(celsius):
    return celsius + 273.15

# Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Función para convertir de Fahrenheit a Kelvin
def fahrenheit_a_kelvin(fahrenheit):
    celsius = fahrenheit_a_celsius(fahrenheit)
    return celsius_a_kelvin(celsius)

# Función para convertir de Kelvin a Celsius
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

# Función para convertir de Kelvin a Fahrenheit
def kelvin_a_fahrenheit(kelvin):
    celsius = kelvin_a_celsius(kelvin)
    return celsius_a_fahrenheit(celsius)

# Función principal del programa
def main():
    temperatura = float(input("Ingrese la temperatura: "))
    escala_actual = input("Ingrese la escala actual (K, C, F): ").upper()
    escala_deseada = input("Ingrese la escala a la que se desea convertir (K, C, F): ").upper()

    if escala_actual == escala_deseada:
        print(f"La temperatura es {temperatura} {escala_actual}")
    else:
        if escala_actual == "C" and escala_deseada == "F":
            resultado = celsius_a_fahrenheit(temperatura)
        elif escala_actual == "C" and escala_deseada == "K":
            resultado = celsius_a_kelvin(temperatura)
        elif escala_actual == "F" and escala_deseada == "C":
            resultado = fahrenheit_a_celsius(temperatura)
        elif escala_actual == "F" and escala_deseada == "K":
            resultado = fahrenheit_a_kelvin(temperatura)
        elif escala_actual == "K" and escala_deseada == "C":
            resultado = kelvin_a_celsius(temperatura)
        elif escala_actual == "K" and escala_deseada == "F":
            resultado = kelvin_a_fahrenheit(temperatura)
        else:
            print("Las escalas ingresadas no son válidas.")
            return

        print(f"La temperatura convertida es {resultado:.2f} {escala_deseada}")


main()

# Función para determinar el grupo y calcular el costo con descuento
def determinar_grupo_y_costo(nombre, edad):
    if 10 <= edad <= 17:
        grupo = "Niños"
        costo = 25000
        if edad > 13:
            costo = costo - (costo * 0.08)
        else:
            costo = costo - (costo * 0.15)
    elif 18 <= edad <= 50:
        grupo = "Adultos"
        costo = 35000
        if edad > 30:
            costo = costo - (costo * 0.09)
        else:
            costo = costo - (costo * 0.11)
    elif edad > 50:
        grupo = "Adulto Mayor"
        costo = 50000
        if edad > 65:
            costo = costo - (costo * 0.40)
    else:
        grupo = "No es elegible para ningún grupo"
        costo = 0

    print(f"Nombre: {nombre}")
    print(f"Grupo: {grupo}")
    print(f"Valor del grupo: {costo:.2f} pesos")
    if costo > 0:
        print(f"Valor a pagar con descuento aplicado: {(costo):.2f} pesos")

# Función principal del programa
def main():
    nombre = input("Ingrese el nombre del participante: ")
    edad = int(input("Ingrese la edad del participante: "))

    determinar_grupo_y_costo(nombre, edad)


main()



# Función para calcular el volumen del cubo
def calcular_volumen_cubo(lado):
    volumen = lado ** 3
    return volumen

# Función para calcular el volumen del cilindro
def calcular_volumen_cilindro(radio, altura):
    volumen = math.pi * radio ** 2 * altura
    return volumen

# Función para calcular el volumen de la esfera
def calcular_volumen_esfera(radio):
    volumen = (4/3) * math.pi * radio ** 3
    return volumen

# Función principal del programa
def main():
    tipo_recipiente = input("Ingrese el tipo de recipiente (Cubo, Cilindro o Esfera): ").lower()

    if tipo_recipiente == "cubo":
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        volumen = calcular_volumen_cubo(lado)
        print(f"El volumen del cubo es: {volumen:.3f} unidades cúbicas")
    elif tipo_recipiente == "cilindro":
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        volumen = calcular_volumen_cilindro(radio, altura)
        print(f"El volumen del cilindro es: {volumen:.3f} unidades cúbicas")
    elif tipo_recipiente == "esfera":
        radio = float(input("Ingrese el radio de la esfera: "))
        volumen = calcular_volumen_esfera(radio)
        print(f"El volumen de la esfera es: {volumen:.3f} unidades cúbicas")
    else:
        print("Tipo de recipiente no válido.")


main()

# Función para calcular cuántas cajas se necesitan
def calcular_cajas(cantidad_cubos, tipo_caja):
    if tipo_caja == "pequeña":
        capacidad_caja = 5  # Litros
    elif tipo_caja == "mediana":
        capacidad_caja = 7  # Litros
    elif tipo_caja == "grande":
        capacidad_caja = 10  # Litros
    elif tipo_caja == "extragrande":
        capacidad_caja = 15  # Litros
    else:
        print("Tipo de caja no válido.")
        return

    cajas_requeridas = cantidad_cubos / (capacidad_caja * 0.001)  # Conversión de litros a cm cúbicos
    return int(cajas_requeridas)

# Función principal del programa
def main():
    cantidad_cubos = int(input("Ingrese la cantidad de cubos de Rubik a enviar: "))
    tipo_caja = input("Ingrese el tipo de caja (Pequeña, Mediana, Grande o Extragrande): ").lower()

    cajas_necesarias = calcular_cajas(cantidad_cubos, tipo_caja)

    if cajas_necesarias is not None:
        print(f"Se necesitan {cajas_necesarias} cajas {tipo_caja} para el envío.")


main()'''
