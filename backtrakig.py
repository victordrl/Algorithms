import random


filas, columnas = 21, 21

laberinto = [[{'visitada': False, 'pared': True} for _ in range(columnas)] for _ in range(filas)]

direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def es_valido(f, c):
    
    return 0 <= f < filas and 0 <= c < columnas and not laberinto[f][c]['visitada']

def backtracking(f, c):
    
    laberinto[f][c]['visitada'] = True
    laberinto[f][c]['pared'] = False
    
    random.shuffle(direcciones)
    
    # Intentar todas las direcciones en orden aleatorio
    for df, dc in direcciones:
        nf, nc = f + df, c + dc
        
        if es_valido(nf, nc):
            
            laberinto[f + df // 2][c + dc // 2]['pared'] = False
            
            backtracking(nf, nc)  # Continuar explorando en profundidad desde la nueva celda


backtracking(1, 1)

for fila in laberinto:
    print(" ".join("█" if celda['pared'] else " " for celda in fila))
