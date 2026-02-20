import random
# aqui empieza el juego en donde se explica los pasos a seguir

print ("Random Country Word Game")
print ("The rules is that you have to type 15 words and then I will tell you how accurate you were.")
print ("Only one try per word, please think first, respond then")

#donde empieza en 0 tipo contador 
incorrect_word = 0 
correct_word = 0 

#lista de paises random
words = [
    "Colombia",
    "Mexico",
    "Guatemala",
    "España",
    "Alemania",
    "Argentina",
    "Chile",
    "Brasil",
    "Bolivia",
    "Honduras",
    "Panama",
    "Italia",
    "Francia",
    "Cuba",
    "Paises Bajo",
    "China",
    "Japon",
    "Singapur",
    "Uruguay",
    "Canada",
    "Ecuador",
]

#la lista que cree arriba de los paises entonces le pone shuffle randomly

random.shuffle(words) 

word_length = 15

#esto es para poner que si es correcto pues te da punto y si no lo quita y dice incorrect
if user_input == word_length:
    print("Correct!")
    correct_word += 1
else:
    print("Incorrect bro!!! Choose wisely.")
    incorrect_word += 1

# el calculo de los puntos de cuanto saco bien y mal en porcentaje
accuracy = (correct_word / 15) * 100

#El print pone el orden por los comas entonces mientras le agregues el coma se pondra en la misma linea

print("Game Summary")
print("Total correct words:", correct_word)
print("Total incorrect words:", incorrect_word)
print("Results:", accuracy, "%")


#https://stackoverflow.com/questions/18834636/random-word-generator-python
#https://docs.flet.dev/
#https://www.w3schools.com/python/module_random.asp 
