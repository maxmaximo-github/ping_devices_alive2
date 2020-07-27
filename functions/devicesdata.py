#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for ping IPv4 devices..

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Ping IPv4 Branche Offices Devices"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


from os import getcwd
from glob import glob


def devices_data():
    """
    Funcion para la creacion de la estrutura de datos.

    Esta funcion realiza la estructura de datos a partir de archivos
    guardados en la carpeta sucursales.

    Al terminar se regresa "devices_list" para su posterior tratamiento.
    """
    directory = getcwd()
    devices_list = []
    for file_name in glob(f"{directory}/sucursales/*"):
        # Obtener nombre de la sucursal a partir de nombre del archivo.
        tmp_name = file_name.split(f"{directory}/sucursales/")
        tmp_name = tmp_name[-1].split(".txt")
        name_sucursal = tmp_name[0]

        dictionary_sucursal = dict()
        tmp_list = []
        # Leer lineas del archivo de la sucursal en turno y guardar los datos
        # en la lista vacia tmp_list
        for line in open(file=file_name, mode="r"):
            # Quitar "Enters" de las lineas y dividir la linea para obtener
            # valores para la lista.
            data_info = line.strip("\n").split(", ")

            # Determinar si existen lineas vacias.
            if len(data_info) != 1:
                tmp_list.append(data_info)
            # Sino continua el programa.
            else:
                continue

        # Agregar valores al dictionario "dictionary_sucursal"
        dictionary_sucursal[name_sucursal] = tmp_list

        # Agregar dictionary_sucursal como un elemento a la lista
        # devices_list
        devices_list.append(dictionary_sucursal)

    return devices_list
