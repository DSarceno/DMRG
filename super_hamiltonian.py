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

sz = (sc.hbar /2)*np.array([[1,0],[0,-1]])
sp = sc.hbar*np.array([[0,1],[0,0]])
sm = sc.hbar*np.array([[0,0],[1,0]])
H2 = np.kron(sz,sz) + (1/2)*(np.kron(sp,sm) + np.kron(sm,sp))

def Sz(i):
    return np.kron(np.eye(2**(i-1)),sz)

def Sp(i):
    return np.kron(np.eye(2**(i-1)),sp)

def Sm(i):
    return np.kron(np.eye(2**(i-1)),sm)

def H(i):
    if i > 2:
        return np.kron(H(i - 1),np.eye(2)) + np.kron(Sz(i - 1),sz) + (1/2)*( np.kron(Sp(i - 1),sm) + np.kron(Sm(i - 1),sp) )
    elif i == 2:
        return H2
    else:
        return 1

print(len(H(n)))
