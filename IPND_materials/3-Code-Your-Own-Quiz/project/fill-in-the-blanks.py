#!/usr/bin/env python3
"""fill_in_the_blanks.py: A game of filling in the blanks.  Player tries to guess the missing words within a given text."""

__author__ = "Evan Daly"
__email__ = "adoormouse@tuta.io"

from enum import Enum
# Enable debugging by setting 'global_debug = True'
global_debug = False
gui_padding = 49
gui_bar = '=' * gui_padding


class GameLevels(Enum):
    """Defines game difficulty levels Name and Values for QASet()
    https://docs.python.org/3/library/enum.html"""
    Easy = 10
    Medium = 5
    Hard = 2


def DebugMessage(message=""):
    """Displays a debug message if the global variable 'global_debug' is true
       Text Colors: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python"""
    if global_debug:
        print("\033[93m DEBUG: " + message + "\033[0m")


def menu_selection(question="Hello", option=[]):
    """Builds a menu which takes a message [question] with options list [options] and returns the users selected option.
        Quit is always an option"""
    DebugMessage(f"""def:menu_selection | question={question} | option={option}""")

    # Add option='Quit' if does not exist and display the menu
    if "Quit" not in option:
        option.append("Quit")

    def displaymenu(option):
        """Sub function used to manage case Quit was not a given option (User should always be able to quit)"""
        DebugMessage(f"""def:displaymenu | option={option}""")
        print(question)
        print("Options:" + str(option))
        response = input("$> ")

        for opt in option:
            if response.lower() == opt.lower():
                DebugMessage(f"User selected a valid option:{opt}")
                if opt == 'Quit':
                    exit(0)
                return opt
        print(f"{response}, is not a valid option")
        print(gui_bar)
        displaymenu(option)

    return displaymenu(option)


def game_main():
    """Game Session starts with user selecting game difficulty level"""
    DebugMessage("""def:game_main""")
    gamelevels = (list(GameLevels.__members__))

    # Loop though game menu till user quits
    spacing = 13
    while True:
        print(gui_bar)
        print(" " * spacing + "FILL IN THE BLANKS GAME")
        print(gui_bar)

        selection = menu_selection("Select a difficulty level:", gamelevels)
        game_session(selection)


def quizitems(gamelevel):
    """Contains the quiztext and answers set for each gamelevel."""
    DebugMessage(f"""QASet, args: gamelevel={gamelevel}""")

    # TODO Create unique game messages for each level

    if gamelevel == GameLevels.Easy.name:
        quiztext = '''A common first thing to do in a language is display
'Hello {0}!'  In {1} this is particularly easy; all you have to do
is type in:
{2} "Hello {0}!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the {2} command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an {3} file in a browser, but it's
a step in learning {1} syntax, and that's really its purpose.
'''

        answers = {'___1___': 'world',
                   '___2___': 'python',
                   '___3___': 'print',
                   '___4___': 'HTML'
                   }
        attempts = GameLevels.Easy.value
        return quiztext, answers, attempts
    elif gamelevel == GameLevels.Medium.name:
        quiztext = '''  A {0} is created with the def keyword. You specify the 
inputs a {0} takes by adding {1} separated by commas between the parentheses. 
{0}s by default return {2} if you don't specify the value to return. {1} can be 
standard data types such as string, number, dictionary, tuple, and {3} or can be 
more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'function',
                   '___2___': 'variable',
                   '___3___': 'None',
                   '___4___': 'list'
                   }
        attempts = GameLevels.Medium.value
        return quiztext, answers, attempts
    elif gamelevel == GameLevels.Hard.name:
        quiztext = '''When you create a {0}, certain {1}s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a {0}, you almost always include at least the {2} {1}, defining
variables for when {3}s of the {0} get made.  Additionally, you generally
want to create a {4} {1}, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like {5} and {6}, which
allow + and - to be used by {3}s of the {0}.  Similarly, {7},
{8}, and {9} allow {3}s of the {0} to be compared
(with <, >, and ==).'''

        answers = {'___1___':'class',
                   '___2___':'method',
                   '___3___':'__init__',
                   '___4___':'instance',
                   '___5___':'__repr__',
                   '___6___':'__add__',
                   '___7___':'__sub__',
                   '___8___':'__lt__',
                   '___9___':'__gt__',
                   '___10___':'__eq__',
                   }

        attempts = GameLevels.Hard.value
        return quiztext, answers, attempts
    else:
        return -1


def quiz(fill_in_blank_text, blank_item, correct_answer):
    """Boollean object that returns True if user guesses correctly for quizitem in fill_in_blank_text"""
    print(fill_in_blank_text)
    print("")
    guess = input(f"What is your guess for {blank_item}?: ")

    if guess.lower() == correct_answer.lower():
        return True
    return False


def game_session(difficulty_level):
    """Initializes and starts the game based on selected level in GameDifficulty and retrieves the quiz from quizitems"""
    DebugMessage(f"def:game_session | game={difficulty_level}")

    # Verify correct parameters/values are passed in before continuing, exit for debugging
    if difficulty_level not in GameLevels.__members__:
        DebugMessage(f"Invalid game type received {difficulty_level}, exiting...")
        exit(1)

    # Initialize the game session with selected difficulty level.  Get quiz items for myGame variables.
    myGame_FillInBlankText, myGame_answers, myGame_attempts = quizitems(difficulty_level)
    # myGame_answers = list(myGame_answers)
    # Fill-In-The-Blank Message in quizitem
    DebugMessage(f"myGame_FillInBlankMessage= {myGame_FillInBlankText}")
    # The Answers used to match blanks in message
    DebugMessage(f"myGame_answers= {myGame_answers}")
    # Attempts remaining based on GameDifficulty Enum values
    DebugMessage(f"myGame_attempts= {myGame_attempts}")

    print(f"Game Level: {difficulty_level}")

    print(gui_bar)


    my_answer_list = list(myGame_answers.keys())
    my_formatted_text = myGame_FillInBlankText.format(*my_answer_list)

    # TODO is there a better way to track the index? in the iterable for loop?
    index = 0 # used to track which value to replace in text
    # Ask question/answer till all questions are correctly matched or attempts <= 0
    for key, val in myGame_answers.items():
        DebugMessage("key={key}, val={val}")
        print(f"Guesses Remaining: {myGame_attempts}")
        print("")
        # Quiz will ask for user input matching to match the blank item(key) with the correct answer (val)
        while not quiz(my_formatted_text, key, val): # returns true when answer is correct.
            # If answer is incorrect, this loop will repeat and -1 myGameAttempts.
            myGame_attempts -= 1
            print(f"Remaining guesses: {myGame_attempts}")
            print("")
            #  If remaining attempts is 0, end game session
            if myGame_attempts <= 0:
                print(".....Game Over, try again?")
                print("\n\n")
                return 0
        my_answer_list[index] = val

        # When answer correct, loop won't be entered. Replace correct answer in myGame_FillInBlankMessage
        my_formatted_text = myGame_FillInBlankText.format(*my_answer_list)
        print("That is correct!")
        print(gui_bar)
        index += 1

    print(my_formatted_text)
    print("")
    print("Congratulations, you've won! Another Game?")
    print("")


game_main()
