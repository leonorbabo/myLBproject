from myLBproject.lib import try_me
from termcolor import colored

def try_me():

    return 'Hello World, from Leonor first package!'


def who_am_i():

    name = whats_my_name()

    # cannot be tested since the function returns None implicitly
    print(colored(name, "blue"))

def sum(a, b):
    return a+b
