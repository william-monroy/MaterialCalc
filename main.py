from os import system

def limpiar():
    system('cls')

def pausa():
    system('pause')

limpiar()

continuar=True

while(continuar==True):
    limpiar()
    print('''

    ███    ███  █████  ████████ ███████ ██████  ██  █████  ██           ██████  █████  ██       ██████ 
    ████  ████ ██   ██    ██    ██      ██   ██ ██ ██   ██ ██          ██      ██   ██ ██      ██      
    ██ ████ ██ ███████    ██    █████   ██████  ██ ███████ ██          ██      ███████ ██      ██      
    ██  ██  ██ ██   ██    ██    ██      ██   ██ ██ ██   ██ ██          ██      ██   ██ ██      ██      
    ██      ██ ██   ██    ██    ███████ ██   ██ ██ ██   ██ ███████      ██████ ██   ██ ███████  ██████ 

    1 ) Calcular nueva ventana
    2 ) Salir

    ''')
    opcion = int(input('OPCION: '))
    if opcion == 1:
        #CODIGO DE PROGRAMA
        print('Introduce las medidas en cm:\n')
        largo = float(input('Largo: '))
        ancho = float(input('Ancho: '))
        
        if ancho >= 140:
            puente = 40
        else:
            puente = 0

        if largo >= 460:
            corredizos = 3
        elif largo >= 230:
            corredizos = 2
        else:
            corredizos = 1

        # Felpa F-15
        

        # Felpa F-10

        # Silicona

        # Tornillos

        # Tarugos

        # Espigas

        # Juego de Corredizos


    elif opcion == 2:
        continuar = False
    else:
        print('Opcion incorrecta')


