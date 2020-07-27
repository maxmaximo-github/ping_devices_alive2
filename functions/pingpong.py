#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for ping IPv4.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


import os
import subprocess


# Colores para impresion de pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;5;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def pingpong(values_ips):
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    name_device, ip = values_ips

    reply = subprocess.call(
        f"ping -c 3 {ip}",
        shell=True,
        stdout=open('/dev/null', 'w'),
        stderr=subprocess.STDOUT
        )

    if reply == 0:
        print(
            f" {red}El dispositivo {green}{name_device}"
            + f"{red} con la IPv4 {green}{ip} {red}esta vivo. "
            + f"{blue}({red}Ping Success!!!!{blue}){color_reset}")

        # Obtener la ruta actual del proyecto.
        directory = os.getcwd()

        # Crear un archivo en la carpeta tmp/nombre_device+ip
        f = open(file=f"{directory}/tmp/{name_device}_{ip}", mode="w")
        f.write(f"{ip}")
        f.close()

    else:
        print(
            f" {red_blink}El dispositivo {green}{name_device}"
            + f"{red} con la IPv4 {green}{ip} {red_blink}no esta disponible."
            + f" {blue}({green}Ping Fail!!!!{blue}){color_reset}")
