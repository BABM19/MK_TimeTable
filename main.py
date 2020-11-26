from random import randrange, choice
from funciones import *

file_read = open('datos1.csv', 'r')
datos_grupos = cargar_datos(file_read) # Diccionario
#horarios = crear_horarios(datos_grupos)
#horEst = horarios[0]
#horPro = horarios[1]
finish = False

while not finish:
    horarios = crear_horarios(datos_grupos)
    exit = False
    for grupo in datos_grupos:
        #print(grupo+':\n')
        for datos_materia in datos_grupos[grupo]:
            #print(datos_materia)
            for i in range(int(datos_materia[1])):
                intersec = buscar2libres(horarios[0][grupo], horarios[1][datos_materia[2]], 'o')
                if intersec == []:
                    print('Error de compatibilidad')
                    exit = True
                    break
                else:
                    #print(intersec)
                    horarios[0][grupo][intersec[0]-1][intersec[1]-1] = datos_materia[0]
                    horarios[1][datos_materia[2]][intersec[0]-1][intersec[1]-1] = datos_materia[0]+'-'+grupo

        if exit:
            break
    if exit:
        finish = True

print_dicc_matricial(horarios[0])
print_dicc_matricial(horarios[1])
