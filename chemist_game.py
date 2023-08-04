import random


def main() -> None:
    """Chemist game by Wayne Teeter of Ridgecrest, California. Ported to Python by PHR."""

    lives: int = 0
    acid: int
    water: float
    response: float
    difference: float

    # Print the game title and introduction.
    print("\n", " " * 22, "CHEMIST")
    print(" " * 6, "CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
    print("\n" * 3)
    print(" THE FICTITIOUS CHEMICAL KRYPTOCYANIC ACID CAN ONLY BE")
    print(" DILUTED BY THE RATIO OF 7 PARTS WATER TO 3 PARTS ACID.")
    print(" IF ANY OTHER RATIO IS ATTEMPTED, THE ACID BECOMES UNSTABLE")
    print(" AND SOON EXPLODES. GIVEN THE AMOUNT OF ACID, YOU MUST")
    print(" DECIDE WHO MUCH WATER TO ADD FOR DILUTION. IF YOU MISS")
    print(" YOU FACE THE CONSEQUENCES.\n")

    # Start of the game with an infinite loop,
    # each loop represents one round.
    while True:

        # In BASIC,INT(RND(1)*50) return a random integer from 0 to 49 .
        # Use of randint from random module to get the same random integers.
        # Generate a random amount of 'acid' between 0 and 49.
        acid = random.randint(0, 49)

        # Use of mathematical "rule of three" to find the proportion of 'water'.
        # Calculate the correct amount of 'water' using the 7:3 dilution ratio.
        water = 7 * acid / 3

        # Get user input. If the input is an integer, convert it to a float and assign it to 'response'. 
        # If it's not a valid number, ask for input again.
        try:
            response = float(
                input(
                    f"  {acid} LITERS OF KRYPTOCYANIC ACID.   HOW MUCH WATER? "
                ).replace(
                    ",", "."
                )  # Replace coma ',' with dot '.' if exist to input string to be a valid float point.
            )
        except ValueError:
            print(" SOMETHING WENT WRONG, WATER SPILLED OUT. TRY AGAIN!\n")
            continue

        # Calculate the absolute 'difference' between the 'water' proportion and user's 'response'.
        difference = abs(water - response)

        # Check if the 'difference' from the user input is greater than 5% of the 'water' proportion.
        # If yes, the round is lost. Otherwise, the round is won, and the game continues.
        if difference > water / 20:
            print(" SIZZLE!   YOU HAVE JUST BEEN DESALINATED INTO A BLOB")
            print(" OF QUIVERING PROTOPLASM!")
            lives += 1  # Increase the lives count for each wrong answer.
            if lives == 9:  # When the lives count reaches 9, it's "GAME OVER".
                print(" YOUR 9 LIVES ARE USED, BUT YOU WILL BE LONG REMEMBERED FOR")
                print(" YOUR CONTRIBUTIONS TO THE FIELD OF COMIC BOOK CHEMISTRY.")
                break  # Break the loop and exit the game.
            print(" HOWEVER, YOU MAY TRY AGAIN WITH ANOTHER LIFE.")
        else:
            print(" GOOD JOB! YOU MAY BREATH NOW, BUT DON'T INHALE THE FUMES!\n")


if __name__ == "__main__":
    main()
