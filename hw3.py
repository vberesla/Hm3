
def task1():
    try:
        a = 1/0
    except ZeroDivisionError:
        print("Deviation to zero permitted")

def task2():
    try:
        x = 1
    finally:
        print("The finally block will be executed no matter if the try block raises an error or not. The code is legal ")


def task3_4():
    print("task3 - will catch all excepts with any Differentiation  ")

def task6_8():
    try:
        open("words.txt", 'x')
    except FileExistsError:
        pass
    f = open("words.txt", "a")
    f.write(input("Print text in English"))
    f.close()

    #open and read the file after the appending:
    f = open("words.txt", "r")
    print(f.read())
    f.close()

    f = open("words.txt", "a")
    f.write(input("Print text in Hebrew"))
    f.close()

    #open and read the file after the appending:
    f = open("words.txt", "r")
    print(f.read())
    f.close()

# 1. Write the following code: a = 1/0
# a. Build a corresponding try-except block to avoid exception
task1()
# Is the following code legal?
# try:
#     x = 1
# finally:
# print("finally")
task2()
task3_4()
task6_8()