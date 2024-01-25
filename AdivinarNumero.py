import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f'Tus huevos adivina un numerico entre el 1 y el {x} y te llevas esta maravillosa nintendo switch: '))
        if guess > random_number:
            print ('Sorry manin, te pasaste. Bájale un quintal anda rey.')
        elif guess < random_number:
            print('Mi loco te quedaste cortito. Echale ahí parriba.')
    print (f'Ah bueeeeeno que eres adivino no sabia. Enhorabuena aquí tienes tu nintendo por adivinar que el numero era {x}')
    
guess(20)