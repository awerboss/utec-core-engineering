#!/usr/bin/env python3
"""Funciones para añadir contenido a archivos de texto UTF-8."""


def append_write(filename="", text=""):
    """Añade texto al final de un archivo y devuelve los caracteres escritos."""
    with open(filename, "a", encoding="utf-8") as archivo:
        return archivo.write(text)
