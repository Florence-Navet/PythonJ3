def is_prime(n):
    if n <= 1:  # Les nombres <= 1 ne sont pas premiers
        return False
    # Vérifie les diviseurs jusqu'à la racine carrée de n
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

# Afficher les nombres premiers jusqu'à 1000
for n in range(2, 1001):  # Vérifie chaque nombre de 2 à 1000
    if is_prime(n):
        print(n)


   