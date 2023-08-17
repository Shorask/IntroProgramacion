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

ca= float(input(""))'''

#Ejercicio funciones1
'''n1=0
n2=0
n1=int(input("Deme un n1: "))
n2=int(input("Deme un n2: "))'''
def suma(a,b):
  sum=(a+b)
  print("La suma de sus numeros es",sum)


#Ejercicio funciones2
'''n1=0
n2=0
n1=int(input("Deme un n1: "))
n2=int(input("Deme un n2: "))'''
def resta(a,b):
  minus=(a-b)
  print("La resta de sus numeros es",minus)


#Ejercicio funciones3
'''n1=0
n2=0
n1=int(input("Ponga su numero: "))
n2=int(input("Ponga su otro numero: "))'''
def times(a,b):
  x=(a*b)
  print("La multiplicacion de sus numeroses",x)


#Ejercicio funciones4
'''n1=0
n2=0
n1=int(input("Ponga numero entero: "))
n2=int(input("Ponga su otro numero entero: "))'''
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