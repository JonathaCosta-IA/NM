"""
Em um experimento de vibração, um bloco de massa $m$ é preso a uma mola com dureza $k$ e a um amortecedor
com coeficiente de amortecimento $c$, conforme mostrado

Para que o experimento tenha início, o bloco é retirado da posição de equilíbrio e solto. 
A posição do bloco em função do tempo é gravada em uma freqüência
de $5 Hz$ (5 vezes por segundo). 
Os dados no intervalo [4,8]s são dados a seguir.

t=[4. , 4.2, 4.4, 4.6, 4.8, 5. , 5.2, 5.4, 5.6, 5.8, 6. , 6.2, 6.4,
       6.6, 6.8, 7. , 7.2, 7.4, 7.6, 7.8, 8.] 
    
x=[-5.87,-4.23,-2.55,-0.89,0.67,2.09,3.31,4.31,5.06,5.55,5.78,5.77,
    5.52,5.08,4.46,3.72,2.88,2.00,1.10,0.23,-0.59]
Com base nos dados deste experimento calcule:
  A velocidade do bloco é a derivada da posição em relação ao tempo.
  Utilize a fórmula de diferença finita central para calcular a velocidade nos tempos $t = 5$s e $t = 6$ s.
  Escreva um script que calcule a derivada de uma função descrita por um conjunto de pontos. 
  Denomine a função de $dx=derivada(x,y)$,em que $x$ e $y$ são vetores com as coordenadas dos pontos, e $dx$ é um vetor com a derivada $dy/dx$ em
  cada ponto. A função deve calcular a derivada no primeiro e no último ponto usando as fórmulas de diferenças finitas progressiva e regressiva, respectivamente, 
  e usando a fórmula de diferença finita central nos demais pontos. 
  Utilize os pontos fornecidos para calcular a velocidade do bloco em [4,8]s. 
  Calcule a aceleração do bloco a partir da diferenciação da velocidade. 
  Trace um gráfico contendo deslocamento, velocidade e aceleração versus tempo para [4,8].

"""

import numpy as np
import matplotlib.pyplot as plt 

t=[4. , 4.2, 4.4, 4.6, 4.8, 5. , 5.2, 5.4, 5.6, 5.8, 6. , 6.2, 6.4,
6.6, 6.8, 7. , 7.2, 7.4, 7.6, 7.8, 8.] 
desl=[-5.87,-4.23,-2.55,-0.89,0.67,2.09,3.31,4.31,5.06,5.55,5.78,5.77,
5.52,5.08,4.46,3.72,2.88,2.00,1.10,0.23,-0.59]

def deriv(x,y):
    dx=[]
    dx.append((y[1]-y[0])/(x[1]-x[0]))
    for i in range(1,len(x)-1):                 # dif. central
        dx.append( (y[i+1] - y[i-1])/(x[i+1]-x[i-1] ) )
    dx.append( (y[-1]-y[-2])/(x[-1]-x[-2]) )
    return dx

vel=deriv(t,desl)
acel=deriv(t,vel)

#Modelo gráfico manual
plt.subplot(3,1,1)
plt.plot(t,desl,'r',label = "Deslocamento")
plt.title("Deslocamento")
plt.legend()
plt.grid('on')

plt.subplot(3,1,2)
plt.plot(t,vel,'b',label = "Velocidade")
plt.title("Velocidade")
plt.legend()
plt.grid('on')

plt.subplot(3,1,3)
plt.plot(t,acel,'g',label = "Aceleração")
plt.title("Aceleração")
plt.legend()
plt.grid('on')
plt.show()



"""
Alternativa via controle de índice para chamada em laço for

series = [desl, vel, acel]
cores  = ['r', 'b', 'g']
titulos = ["Deslocamento", "Velocidade", "Aceleração"]

for i in range(3):
    plt.subplot(3, 1, i+1)
    plt.plot(t, series[i], cores[i], label=titulos[i])
    plt.title(titulos[i])
    plt.legend()
    plt.grid(True)

plt.show()

Alternativa utilizando compactação via função zip

for i, (y, cor, titulo) in enumerate(zip(series, cores, titulos)):
    plt.subplot(3, 1, i)
    plt.plot(t, y, cor, label=titulo)
    plt.title(titulo)
    plt.legend()
    plt.grid(True)

plt.show()

Alternativa explorando o enumerate a partir de 1.

for i, (y, cor, titulo) in enumerate(zip(series, cores, titulos), start=1):
    plt.subplot(3, 1, i)
    plt.plot(t, y, cor, label=titulo)
    plt.title(titulo)
    plt.legend()
    plt.grid(True)

plt.show()

"""

