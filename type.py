print ("Random Country Word Game")
print ("Lets start with the 1st round")

incorrect_word = 0 
correct_word = 0 
list = [
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

randomOrder = random.shuffle(list) 

#esto es para poner que si es correcto pues te da punto y si no lo quita y dice incorrect
if user_input == word:
    print("Correct!")
    correct_word += 1
else:
    print("Incorrect! Try again. Choose wisely.")
    incorrect_word += 1
accuracy = (correct_word / len(words)) * 100

#El print pone el orden por los comas entonces mientras le agregues el coma se pondra en la misma linea

print("Game Summary")
print("Total correct words:", correct_word)
print("Total incorrect words:", incorrect_word)
print("Results:", accuracy, "%")