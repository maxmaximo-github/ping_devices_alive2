#!/usr/bin/env  python3
"""
This script is create for ping IPv4 devices..

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


from os import name
from os import system


def clean_screen():
    """
    Funcion para limpiar pantalla.

    Funcion que limpia la pantalla de las salidas existentes para mostrar
    solo los resultados que uno desee.

    Se realiza una comprativa para determinar si se corre el comando para
    GNU/Linux o para sistemas con Windows.
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
