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


from functions.cleanscreen import clean_screen
from functions.createtmpfolder import create_tmpfolder
from functions.devicesdata import devices_data
from functions.pingpong import pingpong
from functions.threadconfig import thread_config


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def main():
    """
    Funcion Principal.

    Esta funcion llama a las demas funciones de la carpeta 'functions'.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    # Verificar si existe la carpeta tmp dentro del proyecto
    create_tmpfolder()

    # Limpiar pantalla
    clean_screen()

    # Obtener estructura de datos.
    devices_list = devices_data()

    # Ciclo for
    for devices_item in devices_list:
        for name, values_ips in devices_item.items():
            print(f" {green}{'='*75} {color_reset}")
            print(
                f" {blue}Realizando {green}PING {blue}a los dispositivos"
                + f" de {green}'{name}'{color_reset}")
            print(f" {green}{'='*75}{color_reset}\n")

            thread_config(pingpong, values_ips)

            print(f"\n {green}{'='*75} {color_reset}\n")


if __name__ == '__main__':
    main()
