#Bouche pour nb de 1 à 100
for i in range (1, 101):
    ##verifier si multiple de 3 et 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #verifier si multiple de 3
    elif i % 3 == 0:    
        print("Fizz")
    #verifier si multiple de 5
    elif i % 5 == 0:
        print("BUzz")
    #sinon afficher le nombre
    else:
        print(i)