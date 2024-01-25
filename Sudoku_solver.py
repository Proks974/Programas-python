from pprint import pprint

def find_next_empty(puzzle):
    #encuentra la siguiente fila o columna del puzzle que esté vacia
    # te devuelve fila, columna en una tuple o (none, none) si no hay.
    #indices de 0 al 8
    
    for r in range(9): #0,1,2,....,8
        for c in range (9):
            if puzzle [r][c] == -1:
                return r, c
    return None, None 

def valido(puzzle, guess, fila, col):
    #nos dice si el guess es valido o no
    #empezamos con filas
    valores_fila = puzzle[fila]
    if guess in valores_fila:
        return False
    
    valores_col= []
    for i in range(9):
        valores_col.append(puzzle[i][col])
    valores_col = [puzzle[i][col] for i in range(9)]
    if guess in valores_col:
        return False
    
    #ahora el cuadrado, queremos ver donde empieza el  3x3 y luego hacer un bucle sobre los 3 valores de fila/columna
    fila_start= (fila // 3) * 3 # 1//3 = 0, 5 // 3= 1, ...
    col_start= (col // 3) * 3
    
    for r in range(fila_start, fila_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def resol_sudoku(puzzle):
    #resolvemos sudoku
    #nuestro puzzle es una lista de listas donde cada lista es una fila del sudoku
    #que nos devuelve si la solucion existe o no y muta el puzzle para que sea solucion (si existe)
    
    #primer paso -> escoger el sitio donde hacer un intento
    fila, col = find_next_empty(puzzle)
    # si no hay espacios, hemos acabado ya que no hay inputs validos
    if fila is None:
        return True
    
    #Si hay espacio para poner un input, hacemos prueba
    for guess in range(1,10): #numeros del 1 al 9
        if valido(puzzle, guess, fila, col):
            #si es calido, ponemos el guess en el puzzle
            puzzle[fila][col]= guess
            
            if resol_sudoku(puzzle):
                return True
        #si no vlaido o nuestro acierto no resuelve el sudoku, necesitamos hacer un backtrack y probar otro numero
        puzzle[fila][col]= -1 #reset
    #si ningun numero que hemos probado funciona, el sudoku es irresolvible
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(resol_sudoku(example_board))
    pprint(example_board)