import random 

colors = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(colors)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
    
        if len(guess) != 4:
            print(f"You Must Guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in colors:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count colors in the real code
    for color in real_code:
        color_counts[color] = color_counts.get(color, 0) + 1

    # First pass: correct color and position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # Second pass: correct color in wrong position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and color_counts.get(guess_color, 0) > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempt} tries!")
            break
        print(f"Correct positions: {correct_pos}, Correct colors but wrong positions: {incorrect_pos}")
    else:
        print("you ran out of tries, the code was:", *code)


if __name__ == "__main__":
    game()
   
