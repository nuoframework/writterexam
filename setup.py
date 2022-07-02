import time
import os
from tqdm import tqdm
from time import sleep
from colorama import init, Fore, Back, Style

#Definicion de varibles


#Definicion de funciones

def clear():
    if os.name == "posix":
       os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system("cls")

#Inicio

print("Este programa ha sido creado por @nuoframework, si algun problema persiste abre un Issue en GitHub o contacta con el creador")

nombre = str(input("Inserta el nombre el examen: "))

clear()

file = open(f"C:/Users/viruz/Desktop/{nombre}.txt", "w") #Abrimos el archivo txt que queramos editar

var1 = input("Elige (Reading(R), Listening(L), Reading y Listening(B)): ")

if var1 == "R":
   type = "READING"
   veces = 1
elif var1 == "L":
   type = "LISTENING"
   veces = 1
elif var1 == "B":
   veces = 2
else:
   TypeError
   
clear()

for _ in range(veces):   #Esto indica cuantas veces hay que repetirlo

   notas_reading = []
   notas_listening = []
   
   var2 = input("¿Que vas ha hacer ahora? (Reading(R) o Listening(L)): ")
   
   if var2 == "R":
      type = "READING"
      file.write(f"{nombre} {type}" + os.linesep)
   elif var2 == "L":
      type = "LISTENING"
      file.write(f"{nombre} {type}" + os.linesep)
   
   time.sleep(1)
   clear()
   
   if var2 == "R":
      print("")
      for i in [1, 2, 3, 4]:
          nota_r = input(f"¿Que nota has sacado en la parte {i} del" + Style.BRIGHT + " Reading " + Style.RESET_ALL + "?: ")
          print("")
          file.write(f"Nota {i}º Parte: {nota_r}/5" + os.linesep)
          notas_reading.append(int(nota_r)) 
      
      for a in [5, 6]:
         nota_r = input(f"¿Que nota has sacado en la parte {a} del" + Style.BRIGHT + " Reading " + Style.RESET_ALL + "?: ")
         print("")
         file.write(f"Nota {a}º Parte: {nota_r}/6" + os.linesep)
         notas_reading.append(int(nota_r))
      total_r = sum(notas_reading)
      porcent_r = total_r * 100 / 32
      file.write(os.linesep + f"Total de Pntos: {total_r}/32 ---> {porcent_r}% de aciertos")
   
   elif var2 == "L":
      print("")
      for e in [1]:
         nota_l = input(f"¿Que nota has sacado en la parte {e} del" + Style.BRIGHT + " Listening " + Style.RESET_ALL + "?: ")
         print("")
         file.write(f"Nota {e}º Parte: {nota_l}/7" + os.linesep)
         notas_listening.append(int(nota_l))
      
      for o in [2, 3, 4]:
         nota_l = input(f"¿Que nota has sacado en la parte {o} del" + Style.BRIGHT + " Listening " + Style.RESET_ALL + "?: ")
         print("")
         file.write(f"Nota {o}º Parte: {nota_l}/6" + os.linesep)
         notas_listening.append(int(nota_l))
      total_l = sum(notas_listening)
      porcent_l = total_l * 100 / 25
      file.write(os.linesep + f"Total de Pntos: {total_l}/25 ---> {porcent_l}% de aciertos")
   
   else:
      TypeError

file.close()

clear()
print("Se van a mostrar los resultados totales\n")
clear()

for i in tqdm(range(0, 100), initial = 0, 
              desc ="Procesando Resultados"):
    sleep(0.03)

if var1 == "R":
   reading_sobrediez = total_r * 10 / 32
   print("")
   print("El total de puntos de la parte de" + Fore.RED + " READING " + Fore.RESET + "es de: " + Fore.RED + f" {total_r}/32 " + Fore.RESET + f", esta nota sobre 10 es de {reading_sobrediez}")
elif var1 == "L":
   listening_sobrediez = total_l * 10 / 25
   print("")
   print("El total de puntos de la parte de" + Fore.RED + " LISTENING " + Fore.RESET + "es de: " + Fore.RED + f" {total_l}/25 " + Fore.RESET + f", esta nota sobre 10 es de {listening_sobrediez}")
elif var1 == "B":
   reading_sobrediez = total_r * 10 / 32
   listening_sobrediez = total_l * 10 / 25
   print("")
   print("El total de puntos de la parte de" + Fore.RED + " READING " + Fore.RESET + "es de: " + Fore.RED + f" {total_r}/32 " + Fore.RESET + f", esta nota sobre 10 es de {reading_sobrediez}\n\nEl total de puntos de la parte de" + Fore.RED + " LISTENING " + Fore.RESET + "es de: " + Fore.RED + f" {total_l}/25 " + Fore.RESET + f", esta nota sobre 10 es de {listening_sobrediez}")
else:
   TypeError

print("\nToda la informacion obtenida y generada se ha guardado en el archivo: " + Fore.YELLOW + f"{nombre}.txt" + Fore.RESET + "\n")

SystemExit



   
   




   






