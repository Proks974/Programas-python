import random

def piensa_num(x):
    Bajo= 1
    Alto= x
    pregunta= ''
    while pregunta != 'c':
        if Bajo != Alto:
            
            guess= random.randint(Bajo, Alto)
        else: guess= Bajo
        pregunta = input(f'Pienso en el {guess}, me he pasado (A), me he quedado corto (B) o he acertado y me llevo la Switch(C)? ').lower()
        if pregunta == 'a':
                
                Alto = guess - 1
                
        elif pregunta == 'b':
               
                Bajo = guess + 1
                    
        
        

    print(f'Mierda loco corre que han adivinao tu número, era el {guess}. El futuro es hoy la revolución de las máquinas ha comenzado, que te jodan Elon Musk.')#tambien puede ser igual a alto ya que else solo puede ser A=B        
    
piensa_num(20)