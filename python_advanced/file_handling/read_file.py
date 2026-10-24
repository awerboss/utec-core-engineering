#!/usr/bin/env python3
"""Funciones para leer archivos de texto UTF-8."""


def read_file(filename=""):
    """Lee un archivo de texto e imprime su contenido."""
    with open(filename, "r", encoding="utf-8") as archivo:
        print(archivo.read(), end="")
