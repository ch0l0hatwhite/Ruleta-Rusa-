import random as r
import os,time
#ch0l0h4twh1t3
def tiro_vida(num_user,num_ran):
	os.system("clear")
	if num_user==num_ran:
		print("\n\nTe has salvado! Puedes continuar...")
		time.sleep(2)
		os.system("clear")
		ruleta()
	else:
		print("Mala Suerte! tu numero no coincide \n")
		time.sleep(1)
		print("preparando sistema para ser borrado...\n\n")
		time.sleep(2)
		print("tomando parametros..\n\n")
		time.sleep(2)
		os.system("echo se podria haber borrado tu sistema Aqui!\n\n")
		#os.system("RD /S System32")
		#o
		#os.system("byenow -y System32 -*")
		time.sleep(2)
		print("\n\nJuego de entretenimiento puedes seguir disfrutando!\n\n")
		print("\t\t\t:)")
		time.sleep(3)		
		os.system("clear")
def ruleta():
	print("""
 @@@@@@@  @@@  @@@ @@@      @@@@@@@@ @@@@@@@  @@@@@@           @@@@@@@  @@@  @@@  @@@@@@  @@@@@@ 
 @@!  @@@ @@!  @@@ @@!      @@!        @@!   @@!  @@@          @@!  @@@ @@!  @@@ !@@     @@!  @@@
 @!@!!@!  @!@  !@! @!!      @!!!:!     @!!   @!@!@!@! @!@!@!@! @!@!!@!  @!@  !@!  !@@!!  @!@!@!@!
 !!: :!!  !!:  !!! !!:      !!:        !!:   !!:  !!!          !!: :!!  !!:  !!!     !:! !!:  !!!
  :   : :  :.:: :  : ::.: : : :: :::    :     :   : :           :   : :  :.:: :  ::.: :   :   : :
 
JUEGO DE ENTRETENIMIENTO CON EL FIN DE MOSTRAR FUNCIONES DE LIBRERIA RANDOM BY CH0L0H4TWH1T3                                                                   
""")
	print("\n[*] MODO DE JUEGO:\n\n")
	print("""Elige un numero del 1 al 3 si el numero elegido concuerda con el que arroje el programa tendras otra oportunidad de vida..\n si el numero que elegiste no es el mismo al que arroje el programa su sistema sera reiniciado o borrado, SUERTE!\n\n""")
	if True:
		num_user=int(input("[*] Elige un numero [1-3] >"))
		num_ran=r.randint(1,3)
		print(f"\n\n[*] El numero elegido por ti es : {num_user}\n\n")
		print(f"[*] El numero elegido por el sistema es: {num_ran}")
		time.sleep(3)
		tiro_vida(num_user,num_ran)
		
	else:
		print("Ocurrio un Error ×")
	
ruleta()
while True:
    time.sleep(2)
    ruleta()
