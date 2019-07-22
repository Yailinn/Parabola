from numpy import array, linspace
from math import sin, cos, pi, atan
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.02 #Radio de la esfera

def func (conds, t, g,phi): #Función que devuelve valores de theta y omega(arreglo)
    #phi=atan(2*conds[0])
    dx=conds[1]
    db=g*sin(atan(2*conds[0]))*cos(atan(2*conds[0]))
    dy=conds[3]
    dc=-g*(sin(atan(2*conds[0])))**2
    return array([dx,db,dy,dc], float)


g = 9.81
#l = 0.00

thes=0#45*pi/180
phi=0
x=0.0001
y=0.3
b=0
c=0

initcond = array([x,b,y,c], float) #Arreglo de condiciones iniciales

n_steps = 1000 #Número de pasos
t_start = 0.   #Tiempo inicial
t_final = 10.  #Tiempo final
t_delta = (t_final - t_start) / n_steps #Diferencial de tiempo (Paso temporal)
t = linspace(t_start, t_final, n_steps) #Arreglo de diferencial de tiempo

solu, outodeint = odeint( func, initcond, t, args=(g,1), full_output=True) #Solución de la ecuación diferencial(Parámetros acordes a los definidos en la función) 
#solu (Matriz de n filas y 2 columnas) es la solución diferencial para cada paso(columnas) de theta y omega

#print(outodeint['message'])
#print(solu)

xx,bb,yy,cc = solu.T #Devuelve la matriz transpuesta (a cada una de las variables de la izquierda, theta y omega, le define el respectivo vector)


# =====================

scene.range = 0.5 #Tamaño de la ventana de fondo

xp = 0#cos(thes) #Pasa de coordenadas polares a cartesianas
yp = 0.3#sin(thes)
zp = 0.

sleeptime = 0.0001 #Tiempo con que se actualiza la posición de la partícula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.cyan) #Define objeto con que se va a trabajar

time_i = 0 #Contador que se mueve en el espacio temporal en el que se resolvió la ecuación diferencial
t_run = 0  #Tiempo en el que se ejecuta la animación

#for i in range(xx.size):
#	print(xx[i],yy[i])


while t_run < t_final: #ANIMACIÓN
    prtcl.pos = vector( xx[time_i], yy[time_i], zp )

    t_run += t_delta
    sleep(sleeptime)
    time_i += 1
