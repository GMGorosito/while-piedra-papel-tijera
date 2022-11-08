import random
f = open('puntuje.txt' ,'a',encoding='utf8')

while True:
    for i in range (1,4):
        user_action=input("Seleccione (piedra-papel-tijera)")
        posible_actions = ["piedra","papel","tijera"]
        computer_action = random.choice(posible_actions)
        # print(computer_action)
        print("\nTu elegiste", user_action, " , la computadora elegio", computer_action,"\n")
        if user_action == computer_action:
            print(" Empate ! " ,user_action,  ". Ambos Ganaron ! ")
            f.write("Empate.\n")
        elif user_action == "piedra" and computer_action == "papel":
            f.write("Gano la computadora.\n")
            print("Gano la computadora . \n")

        elif user_action == "piedra" and computer_action == "tijera":
            f.write("Gano el usuario.\n")
            print("Gano el usuario . \n")

        elif user_action == "papel" and computer_action == "piedra":
            f.write("Gano la computadora.\n")
            print("Gano la computadora . \n")

        elif user_action == "papel" and computer_action == "tijera":
            f.write("Gano la computadora.\n")
            print("Gano la computadora . \n")

        elif user_action == "tijera" and computer_action == "papel":
            f.write("Gano el usuario.\n")
            print("Gano el usuario . \n")

        elif user_action == "tijera" and computer_action == "piedra":
            f.write("Gano el usurio.\n")
            print("Gano el usuario . \n")
        else:
            print("Error seleccione bien ! ")
            f.write("Error seleccione bien!\n")
    play_again=input("desea jugar nuevamente? (s/n): ")
    if play_again.lower () == 'n': 
        break   

