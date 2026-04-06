#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import time

def Calc_FalsaPosicao(f,a,b,imax,tol,graph=1):  
    print('iteração'
          '\t\t a'
          '\t\t\t b'
          '\t\t\t x'
          '\t\t\t f(a)'
          '\t\t f(x)'
          '\t\t f(b)'
          '\t\t Erro'
          )
    print(100*'-')
    
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

            # print('\t%d\t\t%.3f \t\t%.3f  \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.6f' 
                  # %(i,a,b,x,fa,fb,fx,toli))
            
            print(f'\t{i}'
            f'\t\t {a:2.4f}'
            f'\t\t {b:2.4f}'
            f'\t\t {x:2.4f}'
            f'\t\t {f(a):2.4f}'
            f'\t\t {f(b):2.4f}'
            f'\t\t {f(x):2.4f}'
            f'\t\t {toli:2.4f}'
            )

            dados.append((i,a,b,x,fa,fb,fx,toli))

            if (fa*fx>0): a=x
            else: b=x

            if(toli<tol):           
                print(60*'-')
                print()
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
            plt.title('Falsa Posição (Regula Falsi)')
            plt.legend()
            plt.grid(True)

            plt.show()   # gráfico abre DEPOIS da saída

#%% =============================================================================                       
if __name__== "__main__":

    f= lambda x: 8-4.5*(x - np.sin(x))
    a, b = 2, 3
    
    Calc_FalsaPosicao(f,a,b,imax=500,tol=1e-6,graph=1)