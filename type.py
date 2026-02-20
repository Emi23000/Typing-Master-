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

word_length = 21

#esto me confundiooo muchooooo pero logre llegarle
for country in words:

    answer = input("Type this country: " + country + " : ")

    if answer == country:
        print("Correct!")
        correct_word = correct_word + 1
    else:
        print("Incorrect! Try to be more accurate")
        incorrect_word = incorrect_word + 1


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
#https://www.youtube.com/watch?v=piJc18hcH0Y
#https://www.youtube.com/watch?v=KzqSDvzOFNA
#https://www.youtube.com/watch?v=5W8cy2tYsAM&pp=ygUcd3JpdGUgcmFuZG9tIHdvcmRzIGluIHB5dGhvbtIHCQmiCgGHKiGM7w%3D%3D
#https://chatgpt.com/share/6997bb96-53e0-8008-bee8-8294ee25cabe

