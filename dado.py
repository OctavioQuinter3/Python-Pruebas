import random

press="Si"
while press=="Si" or press=='si' or press=='Si':
    press=input("Quieres lanzar el dado? Escribe Si: ")
    if press=="Si" or press=='si' or press=='Si':
        hidden = random.randrange(1,6)
        print(hidden)
    