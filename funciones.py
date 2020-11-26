from random import randrange, choice

def matriz_2_str(matriz):

    """Recibe una matriz como argumento y devuelve una cadenade caracteres con
    la matriz imprimible"""

    cadena = ''
    for i in range(len(matriz)):
        cadena += '['
        for j in range(len(matriz[i])):
            cadena += '{:>10s}'.format(str(matriz[i][j]))
        cadena += ']\n'
    return cadena

def print_dicc_matricial(datos_grupos):

    """Recibe un diccionario matricial como argumento he imprime las matrices
    como strings"""

    for grupo in datos_grupos:
        print(grupo+':')
        print(matriz_2_str(datos_grupos[grupo]))

def cargar_datos(file_read):

    """Recibe un archivo como argumento y devuelve un diccionario con los datos
    de la tabla cargados"""

    dicc = {}
    materias = []
    horas = []
    profesores = []
    first = True
    for linea in file_read:
        aux = '' #Horas
        aux2 = '' #Profesor
        if first:
            for char in linea[1:]:
                if char == ';' or char == '\n':
                    materias.append(aux)
                    aux = ''
                else:
                    aux += char
            first = False
        else:
            for char in linea[linea.find(';')+1:]:
                if char == ';' or char == '\n':
                    horas.append(aux)
                    profesores.append(aux2)
                    aux = ''
                    aux2 = ''
                elif char.isdigit():
                    aux += char
                elif char.isalpha():
                    aux2 += char
                else:
                    pass
            dicc[linea[:linea.find(';')]] = list(zip(materias, horas, profesores))
            horas = []
            profesores = []
    return dicc

def crear_horarios(datos_grupos):

    """Recibe un diccionario matricial como argumento y devuelve un diccionario
    matricial con horarios vacios"""

    horarios1 = {}
    horarios2 = {}
    for grupo in datos_grupos:
        horarios1[grupo] = []
        if int(grupo[0]) > 0 and int(grupo[0]) < 6:
            for i in range(6):
                horarios1[grupo].append(['-','-','-','-','-'])
        elif int(grupo[0]) > 5 and int(grupo[0]) < 12:
            for i in range(7):
                horarios1[grupo].append(['-','-','-','-','-'])

    profesores = []
    for i in datos_grupos:
        for j in datos_grupos[i]:
            if not j[2] in profesores:
                profesores.append(j[2])
    for profesor in profesores:
        horarios2[profesor] = []
        for i in range(7):
            horarios2[profesor].append(['-','-','-','-','-'])
    return [horarios1, horarios2]

def buscar_libres(horario, str):

    """Recibe una matriz como argumento y devuelve una lista de tuplas (con
    argumento 'l') o una unica tupla aleatoria de la lista (con argumento 'o')
    con las casillas libres ('-')"""

    k = 1
    libres = []
    for i in horario:
        j = 1
        for h in i:
            if h == '-':
                libres.append([k,j])
            j += 1
        k += 1
    if str == 'l': #"list"
        return libres
    elif str == 'o': #"one"
        if libres == []:
            return []
        else:
            return choice(libres)
    else:
        return 0

def buscar_intersecciones(hor1, hor2, str): #en prueba

    """Devuelve lista de espacios libres o solo uno de los datos libres"""

    libre1 = buscar_libres(hor1, 'l')
    libre2 = buscar_libres(hor2, 'l')
    libres = []
    if libre1 == [] or libre2 == []:
        return []
    else:
        for i in libre1:
            if i in libre2:
                libres.append(i)
        if str == 'l': #"list"
            return libres
        elif str == 'o': #"one"
            if libres == []:
                return []
            else:
                return choice(libres)
        else:
            return 0
