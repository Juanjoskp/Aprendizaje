ingreso_mensual = 2600
gasto_mensual = 100

resultado = ingreso_mensual - gasto_mensual

print(resultado)

if ingreso_mensual > 2500:
    print("Has alcanzado los ingresos medios")
    if gasto_mensual > 1000:
        print("Gastos muy altos")
    else:
        print("Gastos normales")

    if ingreso_mensual < 2500:
        print("Cuidado con los ingresos")
        if gasto_mensual > 2000:
            print("Gastos muy altos, vas a entrar en perdidas")
        else:
            print("Gastos medios, aguantas")

if ingreso_mensual - gasto_mensual > 1000:
    print("Estás mal, pierdes dinero")
    if ingreso_mensual - gasto_mensual < 500:
        print("Estas mal, pero no pierdes dinero")
    elif ingreso_mensual - gasto_mensual > 500:
        print("Vas bien, continua así")          
    else:
        print("Todo va genial")

if ingreso_mensual - gasto_mensual < 1000:
    print("Estás bien jodido, pierdes dinero")
    if ingreso_mensual - gasto_mensual < 500:
        print("Estas jodido, pero no pierdes dinero")
    elif ingreso_mensual - gasto_mensual > 500:
        print("Estas jodido, continua")          
    else:
        print("Todo va OK")
else:
        print("OK")         

