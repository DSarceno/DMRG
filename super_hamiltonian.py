#	mié 31 ago 2022 15:41:07 CST
#	super_hamiltonian.py
#	Diego Sarceno (dsarceno68@gmail.com)

#	Calculo del Super Hamiltoniano de una candena de spin-1/2
#   se utilizan las relaciones mostradas en la sección 2.4.2 del libro
#   "Strongly Correlated Systems" - A. Avella, F. Mancini.

#	Codificado del texto: UTF8
#	Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
#	Instruciones de Ejecución: no requiere nada mas
#	python3 super_hamiltonian.py n

#	Librerias
import math as m
import numpy as np
import scipy.constants as sc
import sys

# Librerías locales
import matrix as mat

# Input (dimension de la mitad de la lista (super hamiltoniano), toda la lista (hamiltoniano))
n = int(sys.argv[1])

# Operadores asociados a partículas con spin 1/2
# Tomando hbar = 1
sz = (1/2)*np.array([[1,0],[0,-1]]) # Spin projection operator in 'z'
sp = np.array([[0,1],[0,0]]) # Ladder operators
sm = np.array([[0,0],[1,0]])
H2 = np.kron(sz,sz) + (1/2)*(np.kron(sp,sm) + np.kron(sm,sp)) # Hamiltonian for 2 particles of spin-1/2


# Operadores para una partícula añadida a la derecha de una cadena de spins
def Sz(i):
    return np.kron(np.eye(2**(i-1)),sz)

def Sp(i):
    return np.kron(np.eye(2**(i-1)),sp)

def Sm(i):
    return np.kron(np.eye(2**(i-1)),sm)


# Operadores para una particula añadida a la izquierda de una cadena de spins
def SzR(i):
    return np.kron(sz, np.eye(2**(i - 1)))

def SpR(i):
    return np.kron(sp, np.eye(2**(i - 1)))

def SmR(i):
    return np.kron(sm, np.eye(2**(i - 1)))




####               HAMILTONIANO              ####
def H(i):
    # Funcion recursiva para un sistema lineal de spins 1/2
    if i > 2:
        return np.kron(H(i - 1),np.eye(2)) + np.kron(Sz(i - 1),sz) + (1/2)*( np.kron(Sp(i - 1),sm) + np.kron(Sm(i - 1),sp) )
    elif i == 2:
        return H2
    else:
        return 1


####            SUPER HAMILTONIANO           ####
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
        return np.kron(np.eye(2), HR(i - 1)) + np.kron(sz, SzR(i - 1)) + 0.5*( np.kron(sp, SmR(i - 1)) + np.kron(sm, SmR(i - 1)) )
    elif i == 2:
        return H2
    else:
        return 1



# COMBINED
# super_hamiltonian (Eq. 2.35 Strongly Correlated Systems - A. Avella, F. Mancini)
SH = lambda d: np.kron(np.eye(2**d), HL(d)) + np.kron(HR(d), np.eye(2**d)) +\
    np.kron(np.kron(np.kron(np.eye(2**(d - 1)), sz), sz), np.eye(2**(d - 1))) +\
    0.5*( np.kron(np.kron(np.kron(np.eye(2**(d - 1)), sp), sm), np.eye(2**(d - 1))) +\
    np.kron(np.kron(np.kron(np.eye(2**(d - 1)), sm), sp), np.eye(2**(d - 1))) )


print(SH(n))





##
