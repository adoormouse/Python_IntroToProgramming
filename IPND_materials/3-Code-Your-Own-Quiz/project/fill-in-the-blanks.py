from enum import Enum

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
gui_bar = '=' * 50

# Enable debugging by setting 'global_debug = True'
global_debug = True


def DebugMessage(message=""):
    """Displays a debug message if the global variable 'global_debug' is true
       Text Colors: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python"""
    if global_debug:
        print("\033[93m DEBUG: " + message + "\033[0m")


class GameDifficulty(Enum):
    """Defines game difficulty levels Name and Values for QASet()
    https://docs.python.org/3/library/enum.html"""
    Easy = 10
    Medium = 5
    Hard = 3

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
        response = input(">")

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
    """Game Session starts with user slelecting game difficulty level"""
    DebugMessage("""def:game_main""")
    gamelevels = (list(GameDifficulty.__members__))

    # Loop though game menu till user quits
    while True:
        print("\r\r")
        print("Would you like to play a game?")
        print(gui_bar)
        selection = menu_selection("Select a difficulty level:", gamelevels)
        game_session(selection)

def QASet(game_difficulty):
    """Contains the Question and Answers set for each game dificulty.  Need to define a difficulty to execute"""
    DebugMessage(f"""QASet, args: game_difficulty={game_difficulty}""")

    if game_difficulty == GameDifficulty.Easy.name:
        text = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
            adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
            don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
            tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'function',
                   '___2___': 'variable',
                   '___3___': 'None',
                   '___4___': 'something'
                   }
        attempts = GameDifficulty.Easy.value
        return text, answers, attempts
    elif game_difficulty == GameDifficulty.Medium.name:
        text = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
            adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
            don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
            tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'functions',
                   '___2___': 'something',
                   '___3___': 'something',
                   '___4___': 'something'
                   }
        attempts = GameDifficulty.Medium.value
        return text, answers, attempts
    elif game_difficulty == GameDifficulty.Hard.name:
        text = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
            adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
            don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
            tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'functions',
                   '___2___': 'something',
                   '___3___': 'something',
                   '___4___': 'something'
                   }
        attempts = GameDifficulty.Hard.value
        return text, answers, attempts
    else:
        return -1

def game_session(dificulty_level):
    """The begging of a game"""
    DebugMessage(f"def:game_session | game={dificulty_level}")
    # print("\n"*10)
    if dificulty_level not in GameDifficulty.__members__:
        DebugMessage(f"Invalid game type received {dificulty_level}, exiting...")
        exit(1)
    print("Game Level: " + str(dificulty_level))
    print(gui_bar)

    #
    myGame_FillInBlankMessage, myGame_answers, myGame_attempts = QASet(dificulty_level)
    # Fill-In-The-Blank Message used in QuizItem
    print(myGame_FillInBlankMessage)
    # The Answers used to match blanks in message
    print(myGame_answers)
    # Attempts remaining based on GameDifficulty Enum values
    print(myGame_attempts)

    # TODO While myGameAttempts > 0 run game session
    # TODO Game QuizItem checks for user input matching myGameAnswers to question(___#___) against answer
    # TODO If answer is incorrect, -1 myGameAttempts, and repeat.  Otherwise, continue.
    # TODO replace correct answer in myGameQuestion
    # TODO ask next question/answer till all questions are correctly marched or attempts <= 0



game_main()
