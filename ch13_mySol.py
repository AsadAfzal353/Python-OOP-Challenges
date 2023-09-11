from string import ascii_lowercase
from random import choice
import time

class LetterGuessingException(Exception):
    """"The exception base class for the Letter Guessing App"""

class LetterComesAfter(LetterGuessingException):
    pass

class LetterComesBefore(LetterGuessingException):
    pass

class NotALetter(LetterGuessingException):
    pass


class LetterGuessingGame:

    def __init__(self):
        self.start = time.time()
        self.before = 0
        self.after = 0
        self._correct_guess = False

    def play(self):
        computer_choice = self._pick_a_letter()
        user_guess = None 

        while True:
            try:
                user_guess = input().strip().lower()
                self._validate_user_input(computer_choice, user_guess)
                self._correct_guess = True
                break
            except LetterComesAfter:
                print(f"Nope, it was something {self.state}, guess again")
            except LetterComesBefore:
                print(f"Nope, it was something {self.state}, guess again")
            except NotALetter:
                print("Only English alpahbet letters are supported...")
            except KeyboardInterrupt:
                break
        
        print(self._display_performance())
                    

    def _display_performance(self):
        time_taken = time.time() - self.start
        return f"{'That was correct!' if self._correct_guess else 'Game interrupted.'} You played for {round(time_taken, 2)} seconds, made " \
                f"{self.before} before guesses and {self.after} after guesses"
            
    def _validate_user_input(self, computer_choice, user_guess):
        if user_guess not in ascii_lowercase:
            raise NotALetter
        elif user_guess < computer_choice:
            self.before += 1
            self.state = "after"
            raise LetterComesAfter
        elif user_guess > computer_choice:
            self.after += 1
            self.state = "before"
            raise LetterComesBefore
    
    @staticmethod
    def _pick_a_letter():
        print("The computer has chosen a letter from the English alphabet... What do you think it was?")
        return choice(list(ascii_lowercase))
    

if __name__=="__main__":
    game = LetterGuessingGame()
    game.play()

    # The computer has chosen a letter from the English alphabet... what do you think it was?
    # i # Nope, it was something before, guess again

    # e
    # Nope, it was something before, guess again

    # a
    # That was correct! You played for 5.09 seconds, and made 0 before guesses and 2 after guesses.

    # game = LetterGuessingGame()
    # game.play()

    # The computer has chosen a letter from the English alphabet... what do you think it was?
    # ad
    # Only English alphabet letters are supported...

    # 12
    # Only English alphabet letters are supported...


    # KeyboardInterrupt % control c depending on your runtime

    # Game interrupted. You played for 5.4 seconds, and made 0 before guesses and 0 after guesses.