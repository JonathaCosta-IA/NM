#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Prof. Jonatha Costa

Método da bisseção
    - Se f(x) for real e contínua no intervalo [x1,x2]
    f(x1 ) e f(x2) tiverem sinais opostos, portanto f(x1 ).f(x2 ) < 0,
    então existe pelo menos uma raiz real entre x1 e x2.
    - A nova solução x é obtida pela média entre x1 e x2. A determinação 
    do novo intervalo é feita pela checagem de f(x1 ).f(x2 ) < 0 para x, x1 e x2.
    - O critério de parada pode ser definido como a diferença de f(x) entre 
    duas iterações subsequentes ou pela sua proximidade com o zero.
 
Use: %matplotlib qt para obter grafico em pop-up       
"""
import matplotlib.pyplot as plt
import numpy as np
import time

def calc_bissec(f,a,b,imax,tol,graph=1):  
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
    t0 = time.process_time()         #   Ligar cronômetro
    if f(a)*f(b)>0:
        print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
        print('Por favor teste um novo intervalo [a,b].')
    else:
        dados=[]        
        for i in range(1,imax):
            x=(a+b)/2
            toli=(b-a)/2            
            fa,fb,fx = f(a),f(b),f(x)
            dados.append((i,a,b,x,fa,fb,fx,toli))        
            print(
                f"{i:>5}"
                f"{a:>14.4f}"
                f"{b:>14.4f}"
                f"{x:>14.4f}"
                f"{fa:>14.4f}"
                f"{fb:>14.4f}"
                f"{fx:>14.4f}"
                f"{toli:>12.6f}"
            )
            if (f(a)*f(x)<0): b=x        # Raiz localizada entre a e x >> novo b
            else: a=x                    # Raiz localizada entre b e x >> novo a            
            if(toli<tol):           
                print(60*'-'); break        
        print('\nSolução x=',format(x,'.3f'),'encontrada após',i,'iterações!')    
        print('Tempo de processamento computacional:%.4fs\n\n' %(time.process_time()-t0))
        if graph==1:
            sol = x
            x=[dados[i][0] for i in range(len(dados))] # Iterações
            y=[dados[i][3] for i in range(len(dados))] # Atualizações de x
            plt.figure()
            plt.plot(x,y,'o-',label='Valores de x por iteração')
            plt.xlabel('Iterações');plt.ylabel('Valores de x');
            plt.title(f'Bisseção - solução x = {sol:.3f} encontrada com {i} iterações')
            plt.legend()
            plt.grid(True)
            plt.show()     
            
#%% =============================================================================                       
if __name__== "__main__":

    f= lambda x: 8-4.5*(x - np.sin(x))    # ou def fun(x): ...
    a, b = 2, 3
    calc_bissec(f,a,b,imax=500,tol=1e-6,graph=1)  
  




