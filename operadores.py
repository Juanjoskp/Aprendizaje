ingreso_mensual = 2600
gasto_mensual = 300

if ingreso_mensual > 2500:
    print("Has alcanzado los ingresos medios")
elif ingreso_mensual > 2000:
    print("No ha sido un mal mes")
elif ingreso_mensual > 1500:
    print("Cuidado tu fuente de ingresos está empezando a flojear")    
else:
    print("Te has quedado corto de ingresos")    

resultado = ingreso_mensual - gasto_mensual

print(resultado)

#if ingreso_mensual > 2500:
    #if ingreso_mensual - gasto_mensual <0:
        #print("Estás en deficit")
    #elif ingreso_mensual - gasto_mensual > 3000:
        #print("Estás bien, todo en orden")
    #else:
        #print("Cuidado empiezas a gastar demasiado") 

