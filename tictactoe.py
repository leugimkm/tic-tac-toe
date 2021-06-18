el_tablero = [[' ' for f in range(3) ] for c in range(3)]	

def instrucciones(matriz):
    print(f' Bienvenido '.center(47, '='))
    print('Posiciones del tablero: ')
    print(' 7 | 8 | 9')
    print('---+---+---')
    print(' 4 | 5 | 6')
    print('---+---+---')
    print(' 1 | 2 | 3\n')
    input('Presiona "ENTER" para empezar...')

def _mostrar(matriz): #otra forma de mostrar el tablero
    print('+---+---+---+')
    for i in matriz: 
        print('|', end='')
        for j in i:
            print(f'{j:^3}|', end='')
        print('\n+---+---+---+')

def mostrar(m):
    print(f' {m[0][0]} | {m[0][1]} | {m[0][2]}')
    print('---+---+---')
    print(f' {m[1][0]} | {m[1][1]} | {m[1][2]}')
    print('---+---+---')
    print(f' {m[2][0]} | {m[2][1]} | {m[2][2]}')

def limpiar(matriz):
    for i in range(3):
        for j in range(3):
            matriz[i][j] = ' '

def marcar(matriz, posicion, jugador):
    if posicion in (1, 2, 3): 
        matriz[2][posicion-1] = jugador
    elif posicion in (4,5,6): 
        matriz[1][posicion-4] = jugador
    else: 
        matriz[0][posicion-7] = jugador

def esta_vacio(matriz, posicion):
    if posicion in (1, 2, 3):
        return matriz[2][posicion-1] == ' '
    elif posicion in (4, 5, 6):
        return matriz[1][posicion-4] == ' '
    elif posicion in (7, 8, 9):
        return matriz[0][posicion-7] == ' '

def se_lleno(matriz):
    for posicion in range(10):
        if esta_vacio(matriz, posicion): 
            return False
    return True

def es_tres_en_linea(jugador, m):
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2] == jugador:
            return True
        if m[0][i] == m[1][i] == m[2][i] == jugador:
            return True
    if m[2][0] == m[1][1] == m[0][2] == jugador:
        return True
    if m[0][0] == m[1][1] == m[2][2] == jugador:
        return True

def _es_tres_en_linea(jugador, m): #otra forma de verificar
    return ((m[0][0] == m[0][1] == m[0][2] == jugador) or
            (m[1][0] == m[1][1] == m[1][2] == jugador) or
            (m[2][0] == m[2][1] == m[2][2] == jugador) or
            (m[0][0] == m[1][0] == m[2][0] == jugador) or
            (m[0][1] == m[1][1] == m[2][1] == jugador) or
            (m[0][2] == m[1][2] == m[2][2] == jugador) or
            (m[0][0] == m[1][1] == m[2][2] == jugador) or
            (m[2][0] == m[1][1] == m[0][2] == jugador))

def cambiar(jugador):
    if jugador == 'X': 
        return 'O'
    else: 
        return 'X'

def _posicion_en(matriz, jugador):
    while True:
        try:
            posicion=int(input(f'Marcar {jugador} en:'))
            if posicion in (1,2,3,4,5,6,7,8,9): 
                return posicion
            else: 
                raise ValueError('Ingresar una posicion correcta (1 al 9)')
        except ValueError: 
            print('Error! Ingresar un numero (1 al 9)')

def posicion_en(matriz, jugador):
    posicion = ' '
    while posicion not in '1 2 3 4 5 6 7 8 9'.split():
        posicion=input(f'Marcar {jugador} en:')
    return int(posicion)

def resultado(jugador):
    mostrar(el_tablero)
    print(f'El jugador "{jugador}" gano '.center(47, '='))

def quieres_jugar_de_nuevo():
	print('Jugar otra vez? "S" o "N"')
	return input().lower().startswith('s')

def jugar():
    limpiar(el_tablero)
    instrucciones(el_tablero)
    se_esta_jugando = True
    del_jugador = 'X'
    while se_esta_jugando:
        mostrar(el_tablero)
        en_la_posicion = posicion_en(el_tablero, del_jugador)
        if esta_vacio(el_tablero, en_la_posicion):
            marcar(el_tablero, en_la_posicion, del_jugador)
            if es_tres_en_linea(del_jugador, el_tablero):
                resultado(del_jugador)
                se_esta_jugando = False
            else:
                if se_lleno(el_tablero):
                    print('Empate'.center(47, '='))
                    se_esta_jugando = False
            del_jugador=cambiar(del_jugador)
        else: print('Posicion ocupada, marcar de nuevo')

while True:
    jugar()
    if not quieres_jugar_de_nuevo():
        break
