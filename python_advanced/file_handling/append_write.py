#!/usr/bin/env python3
"""Funciones para añadir contenido a archivos UTF-8."""


def append_write(filename="", text=""):
    """Añade texto a un archivo y devuelve la cantidad escrita."""
    with open(filename, "a", encoding="utf-8") as archivo:
        return archivo.write(text)
