import tkinter as tk


def gen_congruencial_mixto_func(tv_congruencial_mixto, numero1, a_numero, c_numero, m_numero, cant):
    for i in range(cant):
        numero2 = numero1 * a_numero
        numero3 = numero2 + c_numero
        numero4 = numero3 % m_numero

        tv_congruencial_mixto.insert('', tk.END, values=(i + 1, numero1, numero2, numero3,  numero4, f'{numero4}/{m_numero}'))
        numero1 = numero4


def gen_congruencial_multiplicativo_decimal(tv_congruencial_multiplicativo, numero1, a_numero, m_numero, cant):
    for i in range(cant):
        numero2 = numero1 * a_numero
        numero3 = numero2 % m_numero

        tv_congruencial_multiplicativo.insert('', tk.END, values=(
            i + 1, numero1, numero2, numero3,  f'{numero3}/{m_numero}'))
        numero1 = numero3


def gen_congruencial_multiplicativo_binario(tv_congruencial_multiplicativo_binario, numero1, a_numero, m_numero, cant):
    for i in range(cant):
        numero2 = numero1 * a_numero
        numero3 = numero2 % m_numero

        tv_congruencial_multiplicativo_binario.insert('', tk.END, values=(i + 1, numero3))
        numero1 = numero3


def gen_congruencial_cuadratico_func(tv_congruencial_cuadratico, numero1, a_numero, b_numero, c_numero, m_numero):
    for i in range(m_numero):
        numero2 = (a_numero * (numero1 ** 2)) + (b_numero * numero1) + c_numero
        numero3 = numero2 % m_numero

        tv_congruencial_cuadratico.insert('', tk.END, values=(i + 1, numero3,  f'{numero3}/{m_numero - 1}'))
        numero1 = numero3


def gen_congruencial_blum_blum_shub_func(tv_congruencial_blum_blum_shub, numero1, a_numero, b_numero, cant):
    for i in range(cant):
        numero2 = numero1 ** 2
        numero3 = numero2 % (a_numero * b_numero)

        tv_congruencial_blum_blum_shub.insert('', tk.END, values=(i + 1, numero3))
        numero1 = numero3
