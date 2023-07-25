"""Natalie Ferraro hello_world.py

hello_world.py is a simple hello world python module.
"""

def hello():
    """hello function prints a hello world message."""
    list = []
    list.append("hello world")
    list.append("welcome to my Python repo on GitHub.")
    list.append("(-_-)")

    for i in list:
        print(i)

if __name__=="__main__":
    hello()