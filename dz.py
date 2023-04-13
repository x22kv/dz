# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def encrypt(text):
    cipher = 3
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + cipher - 65) % 26 + 65)
        else:
            result += chr((ord(char) + cipher - 97) % 26 + 97)
        return result


def decrypt(text):
    cipher = -3
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + cipher - 65) % 26 + 65)
        else:
            result += chr((ord(char) + cipher - 97) % 26 + 97)
        return result