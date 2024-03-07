import random
import art
import words

print(art.logo)

lives = 6

randomWord = random.choice(words.wordList)

display = []
for numOfletters in randomWord:
    display += "_"
endGame = False
while not endGame:
    guess = input("Guess a letter\n").lower()

    for position in range(len(randomWord)):
        letter = randomWord[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in randomWord:
        lives -= 1
        print(f"Wrong , now you have only  {lives} left!")
        print(display)
    if lives == 0:
        endGame = True

        print(f"You Lose!..The word was {randomWord}")



    if "_" not in display:
        endGame = True
        print("You win!")

    print(art.stages[lives])
