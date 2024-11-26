import string

chaine = string.ascii_lowercase * 10  # Alphabet répété 10 fois
i = 1
position = 0
while i + position <= len(chaine):
    print(chaine[position:i + position])
    position += i
    i += 1


#avec a en début de pyramide
import string

chaine = string.ascii_lowercase * 10  
i = 1  
while i <= 27:  
    print(chaine[:i])  
    i += 1  



