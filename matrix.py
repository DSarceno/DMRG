#	mar 13 sep 2022 19:51:04 CST
#	matrix.py
#	Diego Sarceno (dsarceno68@gmail.com)

#	Función que muestra las matrices de la forma tradicional, con
#   parentesis, corchetes, etc. Hecho por Amado Cabrera.

#	Codificado del texto: UTF8
#	Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
#	Instruciones de Ejecución: no requiere nada mas
#	python3 matrix.py

#	Librerias
import math as m
import numpy as np

def matrix_form2(matrix, limiter='p'):
    """
    Pretty print of a matrix with different delimiters depending on 'p', 'b'or 'v'
    """
    if limiter == 'p':
        ls, li = '⎛', '⎝'
        rs, ri = ' ⎞', ' ⎠'
    elif limiter == 'b':
        ls, li = '⎡', '⎣'
        rs, ri = ' ⎤', ' ⎦'
    elif limiter == 'v':
        ls, li = '⎢', '⎢'
        rs, ri = ' ⎥', ' ⎥'
    else:
        ls, li = '⎡', '⎣'
        rs, ri = ' ⎤', ' ⎦'
    max = 0
    for row in matrix:
        for ele in row:
            if len(str(ele)) > max:
                max = len(str(ele))
    print_str = ''
    for i in range(len(matrix)):
        if i == 0:
            print_str += f'{ls}'
        elif i==(len(matrix)-1):
            print_str += f'{li}'
        else:
            print_str += '⎢'
        for j in range(len(matrix[i])):
            print_str += ' {val:^{max}}'.format(val=matrix[i][j], max=max)
        if i == 0:
            print_str += f'{rs}\n'
        elif i==(len(matrix)-1):
            print_str += f'{ri}'
        else:
            print_str += ' ⎥\n'
    print(print_str, end='\n\n')
