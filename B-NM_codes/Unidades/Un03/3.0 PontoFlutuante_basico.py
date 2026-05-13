#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esse código implementa, de forma didática, a conversão de um número decimal 
inteiro para a sua representação em ponto flutuante binário, seguindo o padrão 
IEEE 754 nos formatos 32 bits (simples precisão) e 64 bits (dupla precisão).
@author: Jonatha Costa
"""
num=83
# 01. Encontrar expoente para o formato 1,ddddd x 2^bbb
for i in range(-10,10):
    if num<pow(2,i): # 'i' é o primeiro expoente que passa num, logo usar-se i-1
        exp = i-1
        break

exp_pol_32 = exp+127
exp_pol_64 = exp+1023

# 02. Encontrar o valor da mantissa do ponto flutuante
num_bin = num / pow(2,exp)
mantissa = abs(1-num_bin)
mantissa_bin = ''
while mantissa > 0:
        mantissa *= 2                # Multiplica o valor por 2
        bit = int(mantissa)          # Guarda o valor da parte inteira em bit 
        mantissa_bin += str(bit)     # Armazena bit como string na string 
        mantissa -= bit 

if exp<0:
    print(f'Fomato binário ponto flutuante base 2: {1}.{mantissa_bin}* 2^-{bin(exp)[3:]}')
else:
    print(f'Fomato binário ponto flutuante base 2: {1}.{mantissa_bin}* 2^{bin(exp)[2:]}')     
    
# 03. Bit de sinal
if num < 0: sinal_bit = '1'
else: sinal_bit = '0'    

# 04. Montando o número 32 bits
exponente = format(exp_pol_32,'08b') # Utilizar -1 para reduzir o expoente de 1 unidade      
mantissa = (mantissa_bin).ljust(23, '0') 
ieee754_bin_32 = sinal_bit +'|'+ exponente + '|'+ mantissa      #

# 05. Montando o número 64 bits
exponente = format(exp_pol_64,'11b') # Utilizar -1 para reduzir o expoente de 1 unidade      
mantissa = (mantissa_bin).ljust(52, '0') 
ieee754_bin_64 = sinal_bit +'|'+ exponente + '|'+ mantissa      #

print(ieee754_bin_32)
print(ieee754_bin_64)