#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import time

def Calc_FalsaPosicao(f,a,b,imax,tol,graph=1): 
    print(150*'-')
    print(
    f"{'iteração':>0}"
    f"{'a':>10}"
    f"{'b':>12}"
    f"{'x':>14}"
    f"{'f(a)':>14}"
    f"{'f(x)':>14}"
    f"{'f(b)':>14}"
    f"{'Erro':>14}"
    )         
    print(150*'-')

    t0 = time.process_time()

    if f(a)*f(b)>0:
        print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
        print('Por favor teste um novo intervalo [a,b].')
    else:
        dados=[]        
        for i in range(1,imax):                        
            fa,fb = f(a),f(b)
            x=(a*fb - b*fa) / ( fb-fa )
            fx=f(x)
            toli=(b-a)/2            
            print(
                f"{i:>5}"
                f"{a:>14.4f}"
                f"{b:>14.4f}"
                f"{x:>14.4f}"
                f"{f(a):>14.4f}"
                f"{f(b):>14.4f}"
                f"{f(x):>14.4f}"
                f"{toli:>12.6f}"
                )

            dados.append((i,a,b,x,fa,fb,fx,toli))
            if (fa*fx>0): a=x
            else: b=x
            if(toli<tol):           
                print(150*'-')
                break                            

        print('\nSolução x=',format(x,'.3f'),'encontrada após',i,'iterações!')    
        print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))


        if graph==1:
            it=[dados[i][0] for i in range(len(dados))]
            y=[dados[i][3] for i in range(len(dados))]

            plt.figure()
            plt.plot(it,y,'o-',label='Valores de x por iteração')
            plt.xlabel('Iterações')
            plt.ylabel('Valores de x')
            plt.title(f'Falsa Posição (Regula Falsi) \n Solução x={x:.3f} encontrada com {i} iterações')
            plt.legend()
            plt.grid(True)
            plt.show()   # gráfico abre DEPOIS da saída

#%% =============================================================================                       
if __name__== "__main__":

    f= lambda x: 8-4.5*(x - np.sin(x))
    a, b = 2, 3
    
    Calc_FalsaPosicao(f,a,b,imax=500,tol=1e-6,graph=1)