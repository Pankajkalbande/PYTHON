import random

word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)

print(f"Passt, the solution is {chosen_word}. ")

display = []

for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_game = True
        print("You Win!")