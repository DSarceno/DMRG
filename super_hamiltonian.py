#	mié 31 ago 2022 15:41:07 CST
#	super_hamiltonian.py
#	Diego Sarceno (dsarceno68@gmail.com)

#	Resumen

#	Codificado del texto: UTF8
#	Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
#	Instruciones de Ejecución: no requiere nada mas
#	python3 super_hamiltonian.py

#	Librerias
import math as m
import numpy as np
import scipy.constants as sc
import sys

n = int(sys.argv[1])

sz = (sc.hbar /2)*np.array([[1,0],[0,-1]]) # Spin projection operator in 'z'
sp = sc.hbar*np.array([[0,1],[0,0]]) # Ladder operators
sm = sc.hbar*np.array([[0,0],[1,0]])
H2 = np.kron(sz,sz) + (1/2)*(np.kron(sp,sm) + np.kron(sm,sp)) # Hamiltonian for 2 particles of spin-1/2

def Sz(i):
    return np.kron(np.eye(2**(i-1)),sz)

def Sp(i):
    return np.kron(np.eye(2**(i-1)),sp)

def Sm(i):
    return np.kron(np.eye(2**(i-1)),sm)

def H(i):
    # Funcion recursiva para un sistema lineal de spins 1/2
    if i > 2:
        return np.kron(H(i - 1),np.eye(2)) + np.kron(Sz(i - 1),sz) + (1/2)*( np.kron(Sp(i - 1),sm) + np.kron(Sm(i - 1),sp) )
    elif i == 2:
        return H2
    else:
        return 1

#print(len(H(n)))


####            SUPER HAMILTONIAN           ####
# LEFT BLOCK

def HL(i):
    if i > 2:
        return np.kron(HL(i - 1), np.eye(2)) + np.kron(Sz(i - 1), sz) + 0.5*(np.kron(Sp(i - 1), sm) + np.kron(Sm(i - 1), sp))
    elif i == 2:
        return H2
    else:
        return 1


# RIGHT BLOCK

def HR(i): # EL input de esta función es la dimensión de la base del bloque derecho D_R
    if i > 2:
        return np.kron(np.eye(2), HR(i - 1)) + np.kron(sz, Sz(i - 1)) + 0.5*(np.kron(sp, Sm(i - 1)) + np.kron(sm, Sp(i - 1)))
    elif i == 2:
        return H2
    else:
        return 1



# super_hamiltonian (Eq. 2.35 Strongly Correlated Systems - A. Avella, F. Mancini)
j = 4
DL = 4
DR = 4
L = DL + DR
#H = HL(j + 1) + HR(j + 2) + Sz(j + 1) @ Sz(j + 2) + 0.5*( Sp(j + 1) @ Sm(j + 2) + Sm(j + 1) @ Sp(j + 2) )

'''
H = np.kron(HL(j + 1), np.eye(DR*2)) + np.kron(np.eye(DL*2),HR(j + 2)) + \
    np.kron(np.kron(np.kron(np.eye(DL),sz),sz),np.eye(DR)) + \
    0.5*np.kron(np.kron(np.kron(np.eye(DL),sp),sm),np.eye(DR)) + \
    0.5*np.kron(np.kron(np.kron(np.eye(DL),sm),sp),np.eye(DR))
'''
#print(H)

#H = HL(j + 1) + HR(L - j - 2) + Sz(j + 1) @ Sz(L - j - 2) + 0.5*( Sp(j + 1) @ Sm(L - j - 2) + Sm(j + 1) @ Sp(L - j - 2) )


print(len(HL(j + 1)))
print(len(HR(j + 2)))
print(len(Sz(j + 1)))
print(len(Sz(j + 2)))
'''
print(len(Sz(j + 1) @ Sz(j + 2)))
print(len(0.5*( Sp(j + 1) @ Sm(j + 2) + Sm(j + 1) @ Sp(j + 2) )))
'''
print(H)









##
