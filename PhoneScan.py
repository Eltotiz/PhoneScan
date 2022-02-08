#creado por Eltotiz

import phonenumbers
import os
from phonenumbers import carrier
from phonenumbers import geocoder
import time


os.system("clear")
print("""  ___  _                   ___                
 | . \| |_  ___ ._ _  ___ / __> ___  ___ ._ _ 
 |  _/| . |/ . \| ' |/ ._>\__ \/ | '<_> || ' |
 |_|  |_|_|\___/|_|_|\___.<___/\_|_.<___||_|_|
                                              

""")
print("")

print("          Creado por Eltotiz ")
print("")
print("")
print("""NOTA: No añada caracteres como espacios o (-) solo añadir el prefijo con el (+).""")
print("")
numero = input("Coloque el numero telefonico: ")
print("")


time.sleep(2)
os.system("clear")

print("============================")
print("")
print(f"Numero: {numero}")
print("")
ch_nmber = phonenumbers.parse(numero, "CH")
print("Ciudad / Provincia:")
print(geocoder.description_for_number(ch_nmber, "es"))
print("")
print("Carrier: ")
service_nmber = phonenumbers.parse(numero, "RO")
print(carrier.name_for_number(service_nmber, "es"))
print("")
print("============================")
