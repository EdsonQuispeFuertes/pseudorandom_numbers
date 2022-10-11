def validate_is_number(number):
    return number.isnumeric()


def validate_size_of_number(number1, number2):
    return len(number1) == len(number2) >= 3


def divisible_entre_2_o_5(number):
    return number % 2 == 0 or number % 5 == 0


def validate_a(a_number):
    return (a_number - 1) % 4 == 0


def validate_number_impar(number):
    return number % 2 != 0


def maximo_comun_divisor(a, b):
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


def calcular_periodo_decimal(m_number):
    if m_number % 10 == 0:
        d = 1
        while 10 ** d != m_number:
            d += 1
        if d >= 5:
            return 5 * (10 ** d-2)
        else:
            a = (2 - 1) * (2 ** (d - 1))
            b = (5 - 1) * (5 ** (d - 1))
            return int(minimo_comun_multiplo(a, b))
    else:
        raise "m es un numero invalido para sistema decimal"


def calcular_periodo_binario(m_number):
    if m_number % 2 == 0:
        return int(m_number / 4)
    else:
        raise "m es un numero invalido para sistema binario"


def validar_potencia_de_2(m_number):
    if m_number % 2 == 0:
        d = 1
        while 2 ** d != m_number and 2 ** d <= m_number:
            d += 1
        if 2 ** d == m_number:
            return True
        else:
            raise "m es un numero invalido para sistema congruencial cuadrático"
    else:
        raise "m es un numero invalido para sistema congruencial cuadrático"


def es_primo_relativo(numero1, numero2):
    while numero2 != 0 :
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto

    # si el el resultado es igual a 1 o a -1, son relativos, si no, no.
    return numero1 == 1 or numero1 == -1


def generar_tabla(fields, tv):
    for field in fields:
        tv.column(field, anchor=CENTER, width=80)
        tv.heading(field, text=field, anchor='w')