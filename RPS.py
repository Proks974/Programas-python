import random

while True:
    Yo = input("Escoge entre 'r' para piedra, 'p' para papel y 't' para tijeras. ")
    Maquina = random.choice(['r', 'p', 't'])
    
    if Yo == Maquina:
        print('Empate, habéis escogido lo mismo.')
    
    elif Yo == 'r':
        if Maquina == 't':
            print('Victoria! Roca aplasta a tijeras!')
        else:
            print('Derrota! Papel envuelve a piedra...')
    elif Yo == 'p':
        if Maquina == 'r':
            print('Victoria! Papel envuelve a piedra!')
        else:
            print('Derrota! Tijeras cortan el papel...')
    elif Yo == 's':
        if Maquina == 'p':
            print('Victoria! Tijeras cortan el papel! ')
        else:
            print('Derrota! Roca aplasta a tijeras...')
            
    Otra_partida = input ('Quieres jugar otra partida? (Responde S/N)' )
    if Otra_partida.lower() != 's':
        break