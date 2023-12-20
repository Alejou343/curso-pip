import random

your_option = input('Escoje tu valor --> ')

def rockPapperScissors(user, computer):  
    print(f"You: {user} - vs - Computer: {computer}")
    if user == computer:
        print('Empate')
    elif user == 'piedra':
        if computer == 'papel':
            print('Has perdido contra papel')
        else:
            print('Has ganado contra tijera')
    elif user == 'papel':
        if computer == 'tijera':
            print('Has perdido contra tijera')
        else:
            print('Has ganado contra piedra')
    elif user == 'tijera':
        if computer == 'piedra':
            print('Has perdido contra piedra')
        else:
            print('Has ganado contra papel')
    else:
        print('Opción no válida')

opciones = ('piedra', 'papel', 'tijera')
rockPapperScissors(your_option.lower(), random.choice(opciones))