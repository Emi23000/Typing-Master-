print ("Random Word Game")
print ("Lets start with the 1st round")

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
]

randomOrder = random.shuffle(list) 


if user_input == word:
    print("Correct!")
    correct_word += 1
else:
    print("Incorrect! Try again. Choose wisely.")
    incorrect_word += 1
accuracy = (correct_word / len(words)) * 100

print("Game Summary")
print("Total correct words:", correct_word)
print("Total incorrect words:", incorrect_word)
print("Results:", accuracy, "%")