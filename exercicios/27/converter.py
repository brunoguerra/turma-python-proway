def convert_type(valor):
    if type(valor) is not str:
        raise Exception('Argument invalid')
    try:
        int_valor = int(valor)
        return int_valor
    except:
        pass
    try:
        float_valor = float(valor)
        return float_valor
    except:
        return valor
print(type(convert_type(1.3424)))
print(type(convert_type('1.3424')))