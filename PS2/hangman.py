import string

# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


class Hangman:
    def __init__(self):
        self.word_list = self.load_words()

    def load_words(self):
        """
        Returns a list of valid words. Words are strings of lowercase letters.

        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, "r")
        # line: string
        line = inFile.readline()
        # word_list: list of strings
        word_list = line.split()
        print("  ", len(word_list), "words loaded.")
        return word_list

    def choose_word(self):
        """
        word_list (list): list of words (strings)

        Returns a word from word_list at random
        """
        return random.choice(self.word_list)

    def is_word_guessed(self, secret_word, letters_guessed):
        """
        secret_word: string, the word the user is guessing; assumes all letters are
          lowercase
        letters_guessed: list (of letters), which letters have been guessed so far;
          assumes that all letters are lowercase
        returns: boolean, True if all the letters of secret_word are in letters_guessed;
          False otherwise
        """
        letters_guessed_hash_table = {}

        for letter in letters_guessed:
            letters_guessed_hash_table[letter] = True

        for letter in secret_word:
            if letter not in letters_guessed_hash_table:
                return False

        return True

    def get_guessed_word(self, secret_word, letters_guessed):
        """
        secret_word: string, the word the user is guessing
        letters_guessed: list (of letters), which letters have been guessed so far
        returns: string, comprised of letters, underscores (_), and spaces that represents
          which letters in secret_word have been guessed so far.
        """
        guessed_word_arr = []
        letters_guessed_hash_table = {}

        for letter in letters_guessed:
            letters_guessed_hash_table[letter] = True

        for letter in secret_word:
            if letter not in letters_guessed_hash_table:
                guessed_word_arr.append("_ ")
            else:
                guessed_word_arr.append(letter)

        return "".join(guessed_word_arr)

    def get_available_letters(self, letters_guessed):
        """
        letters_guessed: list (of letters), which letters have been guessed so far
        returns: string (of letters), comprised of letters that represents which letters have not
          yet been guessed.
        """
        letters_guessed_hash_table = {}

        for letter in letters_guessed:
            letters_guessed_hash_table[letter] = True

        all_lowercase_letters = string.ascii_lowercase
        available_letters = []

        for letter in all_lowercase_letters:
            if letter not in letters_guessed_hash_table:
                available_letters.append(letter)

        return "".join(available_letters)

    def hangman(self, secret_word, with_hints=False):
        """
        secret_word: string, the secret word to guess.

        Starts up an interactive game of Hangman.

        * At the start of the game, let the user know how many
          letters the secret_word contains and how many guesses s/he starts with.

        * The user should start with 6 guesses

        * Before each round, you should display to the user how many guesses
          s/he has left and the letters that the user has not yet guessed.

        * Ask the user to supply one guess per round. Remember to make
          sure that the user puts in a letter!

        * The user should receive feedback immediately after each guess
          about whether their guess appears in the computer's word.

        * After each guess, you should display to the user the
          partially guessed word so far.

        Follows the other limitations detailed in the problem write-up.
        """

        vowels = {"a": True, "e": True, "i": True, "o": True, "u": True}
        secret_word_letters = {}

        for letter in secret_word:
            secret_word_letters[letter] = True

        guesses_left = 6
        warnings_left = 3
        letters_guessed = []

        print("Welcome to the game Hangman!")
        print(f"I am thinking of a word that is {len(secret_word)} letters long.")
        print(f"You have {warnings_left} warnings left.")

        while guesses_left > 0 and not self.is_word_guessed(
            secret_word, letters_guessed
        ):
            guessed_word = self.get_guessed_word(secret_word, letters_guessed)
            guessed_letter = input("Please guess a letter: ").lower()

            if with_hints and guessed_letter == "*":
                print("Possible word matches are: ")
                print(self.show_possible_matches(guessed_word))
                continue

            available_letters = self.get_available_letters(letters_guessed)

            print("-------------")
            print(f"You have {guesses_left} guesses left.")
            print(f"Available letters: {available_letters}")

            if not guessed_letter.isalpha():
                if warnings_left > 0:
                    warnings_left -= 1
                    print(
                        f"Oops! That is not a valid letter. You have {warnings_left} warnings left: {guessed_word}"
                    )
                else:
                    guesses_left -= 1
                    print(
                        f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {guessed_word}"
                    )

                continue

            if guessed_letter in letters_guessed:
                if warnings_left > 0:
                    warnings_left -= 1
                    print(
                        f"Oops! You've already guessed that letter. You now have {warnings_left} warnings: {guessed_word}"
                    )
                else:
                    guesses_left -= 1
                    print(
                        f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {guessed_word}"
                    )

                continue

            letters_guessed.append(guessed_letter)

            if guessed_letter not in secret_word_letters:
                if guessed_letter in vowels:
                    # Vowels lose 2 guesses.
                    guesses_left -= 2
                else:
                    # Consonants lose one guess only.
                    guesses_left -= 1

                print(f"Oops! That letter is not in my word.")

                continue

            print(f"Good guess: {self.get_guessed_word(secret_word, letters_guessed)}")

        if self.is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_left * len(secret_word_letters.keys())
            print("------------")
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
        else:
            print("------------")
            print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")

    def match_with_gaps(self, my_word, other_word):
        """
        my_word: string with _ characters, current guess of secret word
        other_word: string, regular English word
        returns: boolean, True if all the actual letters of my_word match the
            corresponding letters of other_word, or the letter is the special symbol
            _ , and my_word and other_word are of the same length;
            False otherwise:
        """
        word1 = my_word.strip().replace(" ", "")
        word2 = other_word.strip()

        word1_letters = {letter: True for letter in word1 if letter != "_"}

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if word1[i] != "_":
                    return False

                if word2[i] in word1_letters:
                    return False

        return True

    def show_possible_matches(self, my_word):
        """
        my_word: string with _ characters, current guess of secret word
        returns: nothing, but should print out every word in word_list that matches my_word
                Keep in mind that in hangman when a letter is guessed, all the positions
                at which that letter occurs in the secret word are revealed.
                Therefore, the hidden letter(_ ) cannot be one of the letters in the word
                that has already been revealed.

        """
        possible_matching_words = []

        for word in self.word_list:
            is_possible_matching_word = self.match_with_gaps(my_word, word)

            if is_possible_matching_word:
                possible_matching_words.append(word)

        if not possible_matching_words:
            return "No matches found"

        return " ".join(possible_matching_words)

    def hangman_with_hints(self, secret_word):
        """
        secret_word: string, the secret word to guess.

        Starts up an interactive game of Hangman.

        * At the start of the game, let the user know how many
          letters the secret_word contains and how many guesses s/he starts with.

        * The user should start with 6 guesses

        * Before each round, you should display to the user how many guesses
          s/he has left and the letters that the user has not yet guessed.

        * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

        * The user should receive feedback immediately after each guess
          about whether their guess appears in the computer's word.

        * After each guess, you should display to the user the
          partially guessed word so far.

        * If the guess is the symbol *, print out all words in word_list that
          matches the current guessed word.

        Follows the other limitations detailed in the problem write-up.
        """
        self.hangman(secret_word, with_hints=True)


if __name__ == "__main__":
    hangman = Hangman()
    secret_word = hangman.choose_word()
    # hangman.hangman(secret_word)
    # print(hangman.match_with_gaps("te_ t", "tact"))
    # print(hangman.match_with_gaps("a_ _ le", "banana"))
    # print(hangman.match_with_gaps("a_ _ le", "apple"))
    # print(hangman.match_with_gaps("a_ ple", "apple"))
    # print(hangman.show_possible_matches("t_ _ t"))
    # print(hangman.show_possible_matches("abbbb_ "))
    # print(hangman.show_possible_matches("a_ pl_ "))
    hangman.hangman_with_hints(secret_word)
###############
