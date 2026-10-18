#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for posicion in range(len(fila)):
            if posicion > 0:
                print(" ", end="")
            print("{:d}".format(fila[posicion]), end="")
        print()
