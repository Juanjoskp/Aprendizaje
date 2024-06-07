#datos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

#brutos
bruto_promedio = 5
bruto_dalto = 3.5

#diferencias duracion

diferencia_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - curso_dalto / otros_cursos_promedio * 100

print("El curos de dalto dura:")
print(f' - el curso de dalto dura un {diferencia_min} % menos que el curso más rápido')
print(f' - el curso de dalto dura un {diferencia_max} % menos que el curso más lento')
print(f' - el curso de dalto dura un {diferencia_promedio} % menos que el curso promedio')
print("----------------------")
#tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // bruto_promedio / 10
#diferencia_brutos
diferencia_bruto_dalto = 100 - curso_dalto * 1000 // bruto_dalto / 10

print(f" - Otros cursos tienen un {tiempo_vacio_promedio} % de tiempo vacio")

#diferencia brutos
print(f' - los cursos de dalto eliminan un {diferencia_bruto_dalto} % de tiempo vacio')
print("----------------------")
#mostrando las diferencias si los cursos duraran 10 horas
print(f" - ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // curso_dalto / 10} % de otros cursos")
print(f" - ver 10 horas de otros cursos equivale a {curso_dalto * 100 // otros_cursos_promedio / 10} % de otros cursos")