#PROGRAMA QUE SUMA VECTORES SABIENDO SUS COORDENADAS
#import msvcrt
import math
print("######################################")
print(" ")
print("LUDEU")
print("PROGRAMA QUE SUMA 2 VECTORES EN 2D SEGUN SUS COORDENADAS ")
print("A continuacion ingrese las cordenadas del primer vector(A): ")

ax1=float(input("Ingresar ax1: "))
ay1=float(input("Ingresar ay1: "))
ax2=float(input("Ingresar ax2: "))
ay2=float(input("Ingresar ay2 :"))

m1=math.sqrt((ax1-ax2)**2+(ay1-ay2)**2)

print("el modulo del vector A es: ",m1)
print(" ")
print("A continuacion ingrese las cordenadas del primer vector(B): ")
bx1=float(input("Ingresar bx1: "))
by1=float(input("Ingresar by1: "))
bx2=float(input("Ingresar bx2: "))
by2=float(input("Ingresar by2 :"))

m2=math.sqrt((bx1-bx2)**2+(by1-by2)**2)
print("El modulo del vector B es: ",m2)

vectorsumaX=(ax2-ax1)+(bx2-bx1)
vectorsumaY=(ay2-ay1)+(by2-by1)
coab=((ax2-ax1)*(bx2-bx1)+(ay2-ay1)*(by2-by1))/(m1*m2)
angulo=(math.acos(coab))*180/(math.pi)
angulofinal=(math.acos(coab))

print(" ")
print("El vector suma  DE A + B es: ",vectorsumaX,"i + ", vectorsumaY,"j")
print("El angulo en sexagesimales que hay entre los dos vectores es:",angulo)

suma=math.sqrt(m1**2+m2**2+2*m1*m2*math.cos(angulofinal)) #angulofinal*(math.pi/180))
print("El módulo del vector suna A+B es:",suma)
print("Click cualquier tecla para cerrar")

#msvcrt.getch()

#813 156 6092
