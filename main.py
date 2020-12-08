
contador = 1
continuar = True

while contador <= 3:
    usuario = input('Usuario: ')
    password = input('Contraseña:')
    if usuario == 'carlos' and password == '17032002':
        print('Gusto en verte de nuevo Carlos')
        contador = 4
        #CODIGO DEL PROGRAMA
        while(continuar == True):
            print('''

            ███    ███  █████  ████████ ███████ ██████  ██  █████  ██           ██████  █████  ██       ██████ 
            ████  ████ ██   ██    ██    ██      ██   ██ ██ ██   ██ ██          ██      ██   ██ ██      ██      
            ██ ████ ██ ███████    ██    █████   ██████  ██ ███████ ██          ██      ███████ ██      ██      
            ██  ██  ██ ██   ██    ██    ██      ██   ██ ██ ██   ██ ██          ██      ██   ██ ██      ██      
            ██      ██ ██   ██    ██    ███████ ██   ██ ██ ██   ██ ███████      ██████ ██   ██ ███████  ██████ 

            1 ) Calcular nueva ventana
            2 ) Salir

            ''')
            opc = int(input('opc: '))
            if opc == 1:
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
                Felpa_F_15 = largo + ((ancho - puente) * 2 )

                # Felpa F-10
                Felpa_F_10 = largo

                # Silicona


                # Tornillos
                if largo <= 100:
                    if puente != 0:
                        tornillos = 2 + 4
                    else:
                        tornillos = 2
                else:
                    if puente != 0:
                        tornillos = round(largo/50) + 4 #Division entera: Ejemplo 120//50 = 2
                    else:
                        tornillos = round(largo/50) #Division entera: Ejemplo 120//50 = 2

                extra = corredizos * 2
                tornillos = tornillos + extra

                # Tarugos
                tarugos = tornillos - 2

                # Espigas
                if puente != 0:
                    espigas = 2
                else:
                    espigas = 0

                # Juego de Corredizos
                juego_corredizo = corredizos
                
                #-------------------------------------------------------------------------
                # REPORTE
                #-------------------------------------------------------------------------
                print('')

                print('''
                            MATERIALES NECESARIOS     
                
                         Felpa F-15  :  {} mts.
                         Felpa F-10  :  {} mts.
                         Tornillos   :  {} und.
                            Tarugos  :  {} und.
                            Espigas  :  {} und.
                Juego de Corredizos  :  {} und.

                '''.format(Felpa_F_15/100, Felpa_F_10/100, tornillos, tarugos, espigas, juego_corredizo))

            elif opc == 2:
                continuar = False
            else:
                print('Opcion incorrecta')

    else:
        print('Sus datos son incorrectos')
        print('Le quedan {} intentos'.format(3-contador))
        if contador == 3:
            print('Comuniquese con el Administrador')
        contador = contador + 1



