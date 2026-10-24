#!/usr/bin/env python3
"""Funciones para escribir archivos de texto UTF-8."""


def write_file(filename="", text=""):
    """Escribe texto en un archivo y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as archivo:
        return archivo.write(text)
