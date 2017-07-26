from enum import Enum
# Enable debugging by setting 'global_debug = True'
global_debug = False

# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
gui_bar = '=' * 49




def DebugMessage(message=""):
    """Displays a debug message if the global variable 'global_debug' is true
       Text Colors: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python"""
    if global_debug:
        print("\033[93m DEBUG: " + message + "\033[0m")

""" Method to use test values [not used]
def DebugSetValue(variable_name, orig_value, new_value):
    if global_debug:
        DebugMessage(f"Setting {variable_name} from {orig_value} to {new_value}")
        return new_value
    return orig_value
"""

class GameLevels(Enum):
    """Defines game difficulty levels Name and Values for QASet()
    https://docs.python.org/3/library/enum.html"""
    Easy = 1
    Medium = 5
    Hard = 2


def menu_selection(question="Hello", option=[]):
    """Builds a menu which takes a message [question] with options list [options] and returns the users selected option.
        Quit is always an option"""
    DebugMessage(f"""def:menu_selection | question={question} | option={option}""")

    # Add option='Quit' if does not exist and display the menu
    if "Quit" not in option:
        option.append("Quit")

    def displaymenu(option):
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
    while True:
        print(gui_bar)
        print(" "*13 + "FILL IN THE BLANKS GAME")
        print(gui_bar)

        selection = menu_selection("Select a difficulty level:", gamelevels)
        game_session(selection)


def quizitems(gamelevel):
    """Contains the quiztext and answers set for each gamelevel."""
    DebugMessage(f"""QASet, args: gamelevel={gamelevel}""")

    # TODO Create unique game messages for each level

    if gamelevel == GameLevels.Easy.name:
        quiztext = '''  A {0} is created with the def keyword. You specify the inputs a {0} takes by
adding {1} separated by commas between the parentheses. {0}s by default return {2} if you
don't specify the value to return. {1} can be standard data types such as string, number, dictionary,
tuple, and {3} or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'function',
                   '___2___': 'variable',
                   '___3___': 'None',
                   '___4___': 'something'
                   }
        attempts = GameLevels.Easy.value
        return quiztext, answers, attempts
    elif gamelevel == GameLevels.Medium.name:
        quiztext = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
        adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
        don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
        tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'functions',
                   '___2___': 'something',
                   '___3___': 'something',
                   '___4___': 'something'
                   }
        attempts = GameLevels.Medium.value
        return quiztext, answers, attempts
    elif gamelevel == GameLevels.Hard.name:
        answers = {'function': '___1___',
                   'something0': '___2___',
                   'something1': '___3___',
                   'something2': '___4___'
                   }
        quiztext = f'''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
        adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
        don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
        tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

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
    """Initializes the game based on selected level in GameDifficulty and retrieves the quiz from quizitems"""
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

    index = 0
    for key, val in myGame_answers.items():
        DebugMessage("key={key}, val={val}")
        print(f"Guesses Remaining: {myGame_attempts}")
        print("")
        # TODO Ask for user input matching to match the blank item with the correct answer
        while not quiz(my_formatted_text, key, val):
            myGame_attempts -= 1
            print(f"Remaining guesses: {myGame_attempts}")
            print("")
            # TODO if remaining attempts is 0, end game session
            if myGame_attempts <= 0:
                print(".....Game Over, try again?")
                print("\n\n")
                return 0
        my_answer_list[index] = val
        my_formatted_text = myGame_FillInBlankText.format(*my_answer_list)
        print("That is correct!")
        print(gui_bar)
        index += 1

    print(my_formatted_text)
    print("")
    print("Congratulations, you've won! Another Game?")
    print("")



    # TODO If answer is incorrect, -1 myGameAttempts, and repeat.  Otherwise, continue.
    # TODO If correct, replace correct answer in myGame_FillInBlankMessage
    # TODO ask next question/answer till all questions are correctly marched or attempts <= 0



game_main()
