palabra=input("Ingrese su palabra/frase: ").lower()

if(palabra==palabra[::-1]):
    print("ES PALÍNDROMO! ")
else:
    print("No es Palíndromo ")