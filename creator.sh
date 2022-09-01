#!/bin/bash

: << 'header'
Autor:			   Diego Sarceno
Fecha:		     31-08-2022
Tipo Archivo:	 Script Bash
Ejecución:		 ./ejercicio2.sh
Resumen:		   Archivo que automatiza la creaci�n de archivos para programar en "c".
header

# Solicitud del nombre del archivo .c
echo Ingrese el nombre del archivo sin extencion
read name

# Creaci�n del header
fecha=$(date)
echo -e "#	$fecha
#	$name.py
#	Diego Sarceno (dsarceno68@gmail.com) \n
#	Resumen \n
#	Codificado del texto: UTF8
#	Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
#	Instruciones de Ejecución: no requiere nada mas
#	python3 $name.py \n
#	Librerias
import math as m
import numpy as np " > $name.py
