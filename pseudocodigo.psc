Algoritmo MaterialCalc
	Definir continuar Como Logico
	Definir contador,opc,puente,corredizos,extra,espigas,juego_corredizo Como Entero
	Definir usuario,password Como Caracter
	Definir ancho,largo,Felpa_F_15,Felpa_F_10,tornillos,tarugos Como Real
	contador <- 1
	continuar <- Verdadero
	Mientras contador<=3 Hacer
		Escribir 'Usuario: '
		Leer usuario
		Escribir 'Contraseña: '
		Leer password
		Si usuario=='carlos' Y password=='17032002' Entonces
			Escribir 'Gusto en verte de nuevo Carlos'
			contador <- 4
			Mientras continuar==Verdadero Hacer
				Escribir 'MATERIAL CALC'
				Escribir '1) Calcular nueva ventana'
				Escribir '2) Salir'
				Escribir 'OPCION: '
				Leer opc
				Si opc==1 Entonces
					Escribir 'Introduce las medidas en cm:'
					Escribir 'Largo: '
					Leer largo
					Escribir 'Ancho: '
					Leer ancho
					Si ancho>=140 Entonces
						puente <- 40
					SiNo
						puente <- 0
					FinSi
					Si largo>=460 Entonces
						corredizos <- 3
					SiNo
						Si largo>=230 Entonces
							corredizos <- 2
						SiNo
							corredizos <- 1
						FinSi
					FinSi
					// Felpa F-15
					Felpa_F_15 <- largo+((ancho-puente)*2)
					// Felpa F-10
					Felpa_F_10 <- largo
					// Tornillos
					Si largo<=100 Entonces
						Si puente!=0 Entonces
							tornillos <- 2+4
						SiNo
							tornillos <- 2
						FinSi
					SiNo
						Si puente!=0 Entonces
							tornillos <- redon(largo/50)+4 // 50 + 4 #Division entera: Ejemplo 120//50 = 2
						SiNo
							tornillos <- redon(largo/50) // 50 #Division entera: Ejemplo 120//50 = 2
						FinSi
					FinSi
					extra <- corredizos*2
					tornillos <- tornillos+extra
					// Tarugos
					tarugos <- tornillos-2
					// Espigas
					Si puente!=0 Entonces
						espigas <- 2
					SiNo
						espigas <- 0
					FinSi
					// Juego de Corredizos
					juego_corredizo <- corredizos
					// REPORTE==================================================
					Escribir ''
					Escribir '		    MATERIALES NECESARIOS'
					Escribir ''
					Escribir '         Felpa F-15  :  ',Felpa_F_15,' mts.'
					Escribir '         Felpa F-10  :  ',Felpa_F_10,' mts.'
					Escribir '          Tornillos  :  ',tornillos,' und.'
					Escribir '			            Tarugos  :  ',tarugos,' und.'
					Escribir '			            Espigas  :  ',espigas,' und.'
					Escribir 'Juego de Corredizos  :  ',juego_corredizo,' und.'
					Escribir ''
				SiNo
					Si opc==2 Entonces
						continuar <- falso
					SiNo
						Escribir 'Opcion incorrecta'
					FinSi
				FinSi
			FinMientras
		SiNo
			Escribir 'Sus datos son incorrectos'
			Escribir 'Le quedan ',3-contador,' intentos'
			Si contador==3 Entonces
				Escribir 'Comuniquese con el Administrador'
			FinSi
			contador <- contador+1
		FinSi
	FinMientras
FinAlgoritmo

