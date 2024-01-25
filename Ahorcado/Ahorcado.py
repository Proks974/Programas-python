import random
from palabrasENG import words
import string
from hangman_visual import lives_visual_dict


def palabra_valida(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def ahorcado():
    word = palabra_valida(words)
    letras = set(word) #para seleccionar las letras en la palabra
    alfabeto = set(string.ascii_uppercase)
    letra_usada = set() #indica la letra que ya has usado para adivinar
    
    vidas= 7
    
    while len(letras) > 0 and vidas > 0:
        
        print('Te quedan', vidas, 'vidas y has usado estas letras: ', ' '.join(letra_usada))
        
        lista_palabras= [letra if letra in letra_usada else '-' for letra in word]
        print(lives_visual_dict[vidas])
        print('Tu palabra: ', ' '.join(lista_palabras))
        
        user_input = input('Adivina una letra: ').upper()
        
        if user_input in alfabeto - letra_usada:
            letra_usada.add(user_input)
            if user_input in letras:
                letras.remove(user_input)
                print('')
            else:
                vidas = vidas - 1
                print('Incorrecto. ')
        elif user_input in letra_usada:
            print('Ya has intentado con esta letra, prueba con otra. ')
        else:
            print('Caracter no válido, prueba con otro. ')
    if vidas == 0:
        print(lives_visual_dict[vidas])
        print(f'Lo siento, has muerto. La palabra era {word}')
    else:
        print(f'Enhorabuena! Has adivinado correctamente la palabra {word}!!')
        
ahorcado()