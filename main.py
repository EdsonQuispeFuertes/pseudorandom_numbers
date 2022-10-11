#IMPORTAMOS "tkinter"
from tkinter import *
import tkinter
from tkinter import ttk

import tkinter as tk

from Constants.generators import *
from Helpers.validations import validate_is_number, validate_size_of_number, validate_number_impar, validate_a, \
    es_primo_relativo, calcular_periodo_decimal, divisible_entre_2_o_5, calcular_periodo_binario
from generators.congruential_generators import gen_congruencial_mixto_func, gen_congruencial_multiplicativo_decimal, \
    gen_congruencial_multiplicativo_binario, gen_congruencial_cuadratico_func, gen_congruencial_blum_blum_shub_func
from generators.non_congruent_generators import cuadrados_medios_func, productos_medios_func, \
    multiplicador_constante_func


def cuadrados_medios_def():
    if validate_is_number(Xo.get()) and validate_is_number(max_cant.get()):
        tam1 = len(Xo.get())
        numero1 = int(Xo.get())
        cant = int(max_cant.get())
        tv_cuadrados_medios.delete(*tv_cuadrados_medios.get_children())
    else:
        raise 'Solo debe ingresar numeros'
    generar_tabla(tabla_cuadrados_medios, tv_cuadrados_medios)
    cuadrados_medios_func(tv_cuadrados_medios, tam1, numero1, cant)
    tv_cuadrados_medios.place(x=450, y=50)
    print("Fin del generador")


def productos_medios_def():
    if validate_is_number(Xo.get()) and validate_is_number(X1.get())\
            and validate_is_number(max_cant.get()) and validate_size_of_number(Xo.get(), X1.get()):
        tam1 = len(Xo.get())
        numero1 = int(Xo.get())
        numero2 = int(X1.get())
        cant = int(max_cant.get())
        tv_productos_medios.delete(*tv_productos_medios.get_children())
    else:
        raise 'Solo debe ingresar numeros, X0 y X1 deben ser del mismo tamaño y mayor a 3'
    generar_tabla(tabla_productos_medios, tv_productos_medios)

    productos_medios_func(tv_productos_medios, tam1, numero1, numero2, cant)

    tv_productos_medios.place(x=450, y=50)
    print("Fin del generador")


def multiplicador_constante_def():
    if validate_is_number(Xo.get()) and validate_is_number(a.get())\
            and validate_is_number(max_cant.get()) and validate_size_of_number(Xo.get(), a.get()):
        tam1 = len(Xo.get())
        numero1 = int(Xo.get())
        a_numero = int(a.get())
        cant = int(max_cant.get())
        tv_multiplicador_constante.delete(*tv_multiplicador_constante.get_children())
    else:
        raise 'Solo debe ingresar numeros, X0 y a deben ser del mismo tamaño y mayor a 3'
    generar_tabla(tabla_multiplicador_constante, tv_multiplicador_constante)

    multiplicador_constante_func(tv_multiplicador_constante, tam1, numero1, a_numero, cant)

    tv_multiplicador_constante.place(x=450, y=50)
    print("Fin del generador")


def gen_congruencial_mixto_def():
    if validate_is_number(Xo.get()) and validate_is_number(a.get()) and validate_is_number(c.get())\
            and validate_is_number(m.get()) and validate_is_number(max_cant.get()):
        numero1 = int(Xo.get())
        a_numero = int(a.get())
        c_numero = int(c.get())
        m_numero = int(m.get())
        cant = int(max_cant.get())
        tv_congruencial_mixto.delete(*tv_congruencial_mixto.get_children())
    else:
        Label(p4, text='Solo debe ingresar numeros').place(x=450, y=280)
        raise 'Solo debe ingresar numeros'

    a_error_message = '                                                                                                '
    c_error_message = '                                                                                                '
    if not validate_number_impar(int(a.get())):
        a_error_message = 'a debe ser entero impar.'
    elif (a_numero % m_numero == 0) and not validate_a(a_numero):
        a_error_message = 'no cumple (a-1) mod 4 = 0 si 4 es un factor de m.'

    if not validate_number_impar(int(c.get())) and not es_primo_relativo(c_numero, m_numero):
        c_error_message = 'c debe ser un entero impar y relativamente primo a m.'

    Label(p4, text=a_error_message).place(x=450, y=300)
    Label(p4, text=c_error_message).place(x=450, y=320)

    generar_tabla(tabla_congruencial_mixto, tv_congruencial_mixto)

    gen_congruencial_mixto_func(tv_congruencial_mixto, numero1, a_numero, c_numero, m_numero, cant)

    tv_congruencial_mixto.place(x=450, y=50)
    print("Fin del generador")


def gen_congruencial_multiplicativo_sistema_decimal():
    if validate_is_number(Xo.get()) and validate_is_number(a.get()) and validate_is_number(m.get()):
        numero1 = int(Xo.get())
        a_numero = int(a.get())
        m_numero = int(m.get())
        tv_congruencial_multiplicativo.delete(*tv_congruencial_multiplicativo.get_children())
        tv_congruencial_multiplicativo_binario.place(x=-1000, y=-1000)
    else:
        raise 'Solo debe ingresar numeros'
    xo_error_message = '                                                                                               '
    if divisible_entre_2_o_5(int(Xo.get())):
        xo_error_message = 'X0 no debe ser divisible entre 2 o 5'
    Label(p5, text=xo_error_message).place(x=450, y=280)
    generar_tabla(tabla_congruencial_multiplicativo, tv_congruencial_multiplicativo)
    cant = calcular_periodo_decimal(m_numero)

    gen_congruencial_multiplicativo_decimal(tv_congruencial_multiplicativo, numero1, a_numero, m_numero, cant)

    tv_congruencial_multiplicativo.place(x=450, y=50)
    print("Fin del generador")


def gen_congruencial_multiplicativo_sistema_binario():
    if validate_is_number(Xo.get()) and validate_is_number(a.get()) and validate_is_number(m.get()):
        numero1 = int(Xo.get())
        a_numero = int(a.get())
        m_numero = int(m.get())
        tv_congruencial_multiplicativo_binario.delete(*tv_congruencial_multiplicativo_binario.get_children())
        tv_congruencial_multiplicativo.place(x=-1000, y=-1000)
    else:
        raise 'Solo debe ingresar numeros'
    xo_error_message = '                                                                                               '
    if divisible_entre_2_o_5(int(Xo.get())):
        xo_error_message = 'X0 no debe ser divisible entre 2 o 5'
    Label(p5, text=xo_error_message).place(x=450, y=280)
    generar_tabla(tabla_congruencial_multiplicativo_binario, tv_congruencial_multiplicativo_binario)
    cant = calcular_periodo_binario(m_numero)

    gen_congruencial_multiplicativo_binario(tv_congruencial_multiplicativo_binario, numero1, a_numero, m_numero, cant)

    tv_congruencial_multiplicativo_binario.place(x=450, y=50)
    print("Fin del generador")


def gen_congruencial_cuadratico_def():
    if validate_is_number(Xo.get()) and validate_is_number(a.get()) and validate_is_number(b.get())\
            and validate_is_number(c.get()) and validate_is_number(m.get()) and validar_potencia_de_2(int(m.get()))\
            and validate_number_impar(int(c.get())) and not validate_number_impar(int(a.get())):
        numero1 = int(Xo.get())
        a_numero = int(a.get())
        b_numero = int(b.get())
        c_numero = int(c.get())
        m_numero = int(m.get())
        tv_congruencial_cuadratico.delete(*tv_congruencial_cuadratico.get_children())
    else:
        raise 'Solo debe ingresar numeros, y X0 no debe ser divisible entre 2 o 5'
    generar_tabla(tabla_congruencial_cuadratico, tv_congruencial_cuadratico)
    gen_congruencial_cuadratico_func(tv_congruencial_cuadratico, numero1, a_numero, b_numero, c_numero, m_numero)

    tv_congruencial_cuadratico.place(x=450, y=50)
    print("Fin del generador")


def gen_congruencial_blum_blum_shub_def():
    if validate_is_number(Xo.get()) and validate_is_number(a.get()) and validate_is_number(b.get())\
            and validate_is_number(max_cant.get()):
        numero1 = int(Xo.get())
        a_numero = int(a.get())
        b_numero = int(b.get())
        cant = int(max_cant.get())
        tv_congruencial_blum_blum_shub.delete(*tv_congruencial_blum_blum_shub.get_children())
    else:
        raise 'Solo debe ingresar numeros, y X0 no debe ser divisible entre 2 o 5'
    generar_tabla(tabla_congruencial_blum_blum_shub, tv_congruencial_blum_blum_shub)

    gen_congruencial_blum_blum_shub_func(tv_congruencial_blum_blum_shub, numero1, a_numero, b_numero, cant)
    tv_congruencial_blum_blum_shub.place(x=450, y=50)
    print("Fin del generador")


def generar_tabla(fields, tv):
    for field in fields:
        tv.column(field, anchor=CENTER, width=80)
        tv.heading(field, text=field, anchor='w')


def add_elements(p, fields):
    pos_x_label = 150
    pos_x_entry = 200
    pos_y = 70

    for field in fields:
        Label(p, text=field).place(x=pos_x_label, y=pos_y)
        if(field == 'Xo'):
            Entry(p, textvariable=Xo).place(x=pos_x_entry, y=pos_y)
        if(field == 'X1'):
            Entry(p, textvariable=X1).place(x=pos_x_entry, y=pos_y)
        elif(field == 'a'):
            Entry(p, textvariable=a).place(x=pos_x_entry, y=pos_y)
        elif(field == 'b'):
            Entry(p, textvariable=b).place(x=pos_x_entry, y=pos_y)
        elif(field == 'c'):
            Entry(p, textvariable=c).place(x=pos_x_entry, y=pos_y)
        elif(field == 'm'):
            Entry(p, textvariable=m).place(x=pos_x_entry, y=pos_y)
        elif(field == 'Max'):
            Entry(p, textvariable=max_cant).place(x=pos_x_entry, y=pos_y)
        pos_y += 30


# VENTANA PRINCIPAL.
root = tkinter.Tk()
root.title("VENTANA CON PESTAÑAS")
root.geometry("1000x400")
nombre = StringVar()
numero = StringVar()
Xo = StringVar()
X1 = StringVar()
a = StringVar()
b = StringVar()
c = StringVar()
m = StringVar()
max_cant = StringVar()


# INCLUIMOS PANEL PARA LAS PESTAÑAS.
nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')


#CREAMOS PESTAÑAS
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)
p5 = ttk.Frame(nb)
p6 = ttk.Frame(nb)
p7 = ttk.Frame(nb)


# ELEMENTOS PESTAÑA Cuadrados Medios.
Button(p1, text='Cuadrados Medios', bg='light blue', command=cuadrados_medios_def).place(x=200, y=250)
tv_cuadrados_medios = ttk.Treeview(p1, columns=tabla_cuadrados_medios, show='headings', height=8)
add_elements(p1, cuadrados_medios)

# ELEMENTOS PESTAÑA Productos Medios.
Button(p2, text='Productos Medios', bg='light blue', command=productos_medios_def).place(x=200, y=250)
tv_productos_medios = ttk.Treeview(p2, columns=tabla_productos_medios, show='headings', height=8)
add_elements(p2, productos_medios)

# ELEMENTOS PESTAÑA Multiplicador Constante.
Button(p3, text='Multiplicador Constante', bg='light blue',command=multiplicador_constante_def).place(x=200, y=250)
tv_multiplicador_constante = ttk.Treeview(p3, columns=tabla_multiplicador_constante, show='headings', height=8)
add_elements(p3, multiplicador_constante)

# ELEMENTOS PESTAÑA Congruencial Mixto.
Button(p4, text='Congruencial Mixto', bg='light blue', command=gen_congruencial_mixto_def).place(x=200, y=250)
tv_congruencial_mixto = ttk.Treeview(p4, columns=tabla_congruencial_mixto, show='headings', height=8)
add_elements(p4, gen_congruencial_mixto)

# ELEMENTOS PESTAÑA Congruencial Multiplicativo.
Button(p5, text='Sistema Decimal', bg='light blue',
       command=gen_congruencial_multiplicativo_sistema_decimal).place(x=50, y=250)
tv_congruencial_multiplicativo = ttk.Treeview(p5, columns=tabla_congruencial_multiplicativo, show='headings', height=8)
Button(p5, text='Sistema Binario', bg='light blue',
       command=gen_congruencial_multiplicativo_sistema_binario).place(x=250, y=250)
tv_congruencial_multiplicativo_binario = ttk.Treeview(p5, columns=tabla_congruencial_multiplicativo_binario,
                                                      show='headings', height=8)
add_elements(p5, gen_congruencial_multiplicativo)

# ELEMENTOS PESTAÑA Congruencial Aditivo.
Button(p6, text='Congruencial Cuadratico', bg='light blue', command=gen_congruencial_cuadratico_def).place(x=200, y=250)
tv_congruencial_cuadratico = ttk.Treeview(p6, columns=tabla_congruencial_cuadratico, show='headings', height=8)
add_elements(p6, gen_congruencial_cuadratico)

# ELEMENTOS PESTAÑA Congruencial Blum, Blum y Shub.
Button(p7, text='Congruencial Blum, Blum y Shub', bg='light blue',
       command=gen_congruencial_blum_blum_shub_def).place(x=200, y=250)
tv_congruencial_blum_blum_shub = ttk.Treeview(p7, columns=tabla_congruencial_blum_blum_shub, show='headings', height=8)
add_elements(p7, gen_congruencial_blum_blum_shub)

# AGREGAMOS PESTAÑAS CREADAS
nb.add(p1, text='Cuadrados Medios')
nb.add(p2, text='Productos Medios')
nb.add(p3, text='Multiplicador Constante')
nb.add(p4, text='Congruencial Mixto')
nb.add(p5, text='Congruencial Multiplicativo')
nb.add(p6, text='Congruencial Cuadratico')
nb.add(p7, text='Congruencial Blum, Blum y Shub')

root.mainloop()
