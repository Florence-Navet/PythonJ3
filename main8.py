#faire rentrer les longeurs à l'utilisateurs
a = float (input("Veuillez entrer la longeur a : "))
b = float (input("Veuillez entrer la longeur b : "))
c = float (input("Veuillez entrer la longeur c : ")) 

#verifier si les longueurs peuvent former des triangles
if a + b > c and a + c > b and b + c > a:

    #verifier si le triangle est rectangle
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Ce triangle est bien rectangle.")

    #verifier si le triangle est equilateral
    elif a == b == c:
        print("Ce triangle est équilatéral.")

    #verifier si le triangle est isocèle
    elif a == b or a == b or b == c:
        print("Ce triangle est isocèle.")

#si aucune des conditions pré ne marchent, il est quelconque.
    else:
        print("Ce triangle est quelconque")  

else:
    print("Les longueurs saisies ne formeront pas un triangle.")     









