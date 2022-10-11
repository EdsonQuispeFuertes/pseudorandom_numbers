import tkinter as tk


def cuadrados_medios_func(tv_cuadrados_medios, tam1, numero1, cant):
    for i in range(cant):
        numero2 = numero1 ** 2
        snumero2 = str(numero2)
        tam2 = len(snumero2)
        primerc = int((tam2 - tam1) / 2)

        snumero3 = snumero2[primerc:primerc + tam1]
        numero_4 = int(snumero3)/10000
        tv_cuadrados_medios.insert('', tk.END, values=(i + 1, numero1, numero2, snumero3,  numero_4))
        numero1 = int(snumero3)


def productos_medios_func(tv_productos_medios, tam1, numero1, numero2, cant):
    for i in range(cant):
        numero3 = numero1 * numero2
        snumero3 = str(numero3)
        tam2 = len(snumero3)
        primerc = int((tam2 - tam1) / 2)

        snumero4 = snumero3[primerc:primerc + tam1]
        numero_5 = int(snumero4)/10000
        tv_productos_medios.insert('', tk.END, values=(i + 1, numero1, numero2, snumero3,  snumero4, numero_5))
        numero1 = numero2
        numero2 = int(snumero4)


def multiplicador_constante_func(tv_multiplicador_constante, tam1, numero1, a_numero, cant):
    for i in range(cant):
        numero2 = numero1 * a_numero
        snumero2 = str(numero2)
        tam2 = len(snumero2)
        primerc = int((tam2 - tam1) / 2)

        snumero3 = snumero2[primerc:primerc + tam1]
        numero_4 = int(snumero3)/10000
        tv_multiplicador_constante.insert('', tk.END, values=(i + 1, numero1, numero2, snumero3,  numero_4))
        numero1 = int(snumero3)
