import time
import endecrypt
import os


def menu():
    print("""

    [1] Convert text to binary
    [2] Convert binary to text

    """)
    choice = input("- ")

    if choice == '1':
        os.system('cls')
        choice1()

    elif choice == '2':
        choice2()

    else:
        print("select a valid option")
        menu()

def choice1():
    print("text:")
    text = input("- ")

    binary = endecrypt.encode(text, 'binary')
    print(binary)
    time.sleep(1)
    os.system('pause')
    menu()

def choice2():
    print("binary:")
    text = input("- ")

    binary = endecrypt.decode(text, 'binary')
    print(binary)
    time.sleep(1)
    os.system('pause')
    menu()

menu()