"""
This script uses the Microsoft Edge browser to search for random words on Google.

Usage:
python msedge_random_word_search.py

Dependencies:
- Python 3
- PyAutoGUI
- requests

Example:
python msedge_random_word_search.py

Enter the number of searches you want to do:5
The program has searched5times
"""
import pyautogui
import time
import requests
import random


def main():
    """
    This function is the main entry point of the script. It opens Microsoft Edge,
    performs the specified number of searches, and then closes Microsoft Edge.

    Parameters:
    None

    Returns:
    None
    """
    searches = input("Enter the number of searches you want to do: ")

    OpenEdge()

    for i in range(int(searches)):
        Search()
        time.sleep(random.randint(25, 30))

    print("The program has made "+searches+" searches.")

    closeEdge()

        


def OpenEdge():
    """
    This function opens the Microsoft Edge browser.

    Parameters:
    None

    Returns:
    None
    """
    edgeLocation = pyautogui.locateOnScreen("data/EdgeLogo.png", confidence=0.8)
    pyautogui.moveTo(edgeLocation)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(3)

def closeEdge():
    """
    This function closes the Microsoft Edge browser.

    Parameters:
        None

    Returns:
        None
    """
    pyautogui.moveTo(1915,0)
    pyautogui.leftClick()
def Word():
    """
    This function makes a GET request to the Random Word API and returns a random word as a string.

    Parameters:
        None

    Returns:
        A random word as a string
    """
    word = requests.get('https://random-word-api.herokuapp.com/word')
    wordToSearch =  word.text;
    wordToSearch = wordToSearch.strip('[]').replace('"', '')
    return wordToSearch

def Search():
    """
    This function uses the pyautogui library to simulate a keyboard press of the 'alt' key and the 'd' key, followed by a delay of 0.2 seconds. It then uses the requests library to make a GET request to the Random Word API and retrieve a random word. The word is then typed into the currently active window using the pyautogui library, with an interval of 0.3 seconds between each character. After a delay of 0.2 seconds, the 'enter' key is pressed.

    Parameters:
        None

    Returns:
        None
    """
    pyautogui.hotkey('alt', 'd')
    time.sleep(0.2)
    pyautogui.typewrite(Word(), interval=0.3)
    time.sleep(0.2)
    pyautogui.press('enter')


main()