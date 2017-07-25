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
gui_bar = '='*50

global_debug = True


def DebugMessage(message=""):
    """Displays a debug message if the global variable 'global_debug' is true"""
    if global_debug:
        print("Debug_Message: "+ message)
    return 0


class GameDifficulty(Enum):
    """Defines game difficulty levels for QASet()
    https://docs.python.org/3/library/enum.html"""
    Easy = 1
    Medium = 2
    Hard = 3


def QASet(game):
    """Contains the Question and Answers set for each game dificulty.  Need to define a difficulty to execute"""
    DebugMessage(f"{QASet.__name__ },  game :{game}")
    game_difficulty = game.name

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
        return text, answers
    elif game_difficulty == GameDifficulty().Medium.name:
        text = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
            adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
            don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
            tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'functions',
                   '___2___': 'something',
                   '___3___': 'something',
                   '___4___': 'something'
                   }
        return text, answers
    elif game_difficulty == GameDifficulty().Hard.name:
        text = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
            adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
            don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
            tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

        answers = {'___1___': 'functions',
                   '___2___': 'something',
                   '___3___': 'something',
                   '___4___': 'something'
                   }
        return text, answers
    else:
        return -1


def game_menu(question="Hello", option=["Test"]):
    """Menu which takes a message [question] with options list [options] and returns the users selected option.
        Quit is always an option"""
    DebugMessage(game_menu.__name__ + " is running")
    number_of_options = len(option)
    # Check if options list and question is empty
    if number_of_options > 0:
        option.append("Quit")
        while True:
            print(question)
            print("Options:"+ str(option))
            response = input(">")

            if response.lower() == option[number_of_options].lower():
                print("Good bye!")
                exit(0)

            for opt in option:
                if opt.lower() == response.lower():
                    print("Valid Response")
                    print(opt)
                    return opt

            print(f"{response}, is not a valid option")
            print(gui_bar)

    else:
        return -1


def game_main():
    """Game Session starts with user slelecting game difficulty level"""
    DebugMessage(game_main.__name__ + " is running")
    DebugMessage("Game Menu started")
    #Loop though game menu till user quits
    while True:
        print("\r\r")
        print("Would you like to play a game?")

        print(gui_bar)
        GameLevel = game_menu("Pick a difficulty", levels)
        gameSession(GameLevel)
        print("\n\n")


def game_session(game):
    DebugMessage(game_session.__name__ + " is running")
    #print("\n"*10)
    print("Game Level: " + str(game))
    print(gui_bar)
    print(QASet(game))

    pass
gameLevels = (list(GameDifficulty.__members__))
MyGame = GameDifficulty.Easy
game_session(MyGame)

print(gameLevels)
