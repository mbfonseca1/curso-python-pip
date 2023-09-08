import random
import time


def animation():
    time.sleep(0.5)
    print("...")
    time.sleep(0.2)
    print("...", "\n")
    time.sleep(1)


def option_selection():
    user = ""
    opciones = ("piedra", "papel", "tijera")
    while user not in opciones:
        print("\n", "-"*30, "\n")
        time.sleep(0.5)
        user = input("Elije una opción: ").lower()

    print("\n")
    print(f"Has elejido            => {user}")
    machine = random.choice(opciones)
    time.sleep(1)
    print(f"Computadora ha elejido => {machine}")
    time.sleep(1)

    return user, machine


def welcome():
    print('   ┌'+'-'*34+'┐   ')
    print('   |Bienvenid@ a PIEDRA, PAPEL, TIJERA|   ')
    print('   └'+'-'*34+'┘   ')
    print('Para jugar escribe: Piedra, Papel o Tijera')
    
    

def round_winner(user, machine, user_score, machine_score):
    if user == machine:
        print("¡¡¡    EMPATE    !!!")
    elif user == "piedra" and machine == "tijera" or \
            user == "papel" and machine == "piedra" or \
            user == "tijera" and machine == "papel":
        user_score += 1
        print("¡¡¡   USUARIO gana ronda   !!!")
    else:
        machine_score += 1
        print("¡¡¡ COMPUTADORA gana ronda !!!")

    time.sleep(1)
    return user_score, machine_score


def match(user_score, machine_score):
    while True:
        user, machine = option_selection()
        animation()
        user_score, machine_score = round_winner(
            user, machine, user_score, machine_score)
        time.sleep(0.5)
        print(f'\n          Usuario: {user_score}')
        print(f'\n          Maquina: {machine_score}')
        time.sleep(1)
        if user_score >= 2 or machine_score >= 2:
            break
    return user_score, machine_score


def show_winner(user_score, machine_score):
    time.sleep(1)
    print("\n    ***************************")
    if user_score > machine_score:
        print("    ***   GANADOR:USUARIO   ***")
    elif user_score < machine_score:
        print("    ***   GANADOR:MAQUINA   ***")
    else:
        print("    ***       EMPATE       ***")
    print("    ***************************\n")
    time.sleep(2)


def run():
    user_score = 0
    machine_score = 0

    welcome()
    user_score, machine_score = match(user_score, machine_score)
    show_winner(user_score, machine_score)


if __name__ == '__main__':
    run()
