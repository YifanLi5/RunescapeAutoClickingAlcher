import pyautogui
import numpy
import random
import time
import os

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

GAME_TICK_INTERVAL = 0.603
DOUBLE_CLICK_INTERVAL = 0.35
DOUBLE_CLICK_INTERVAL_STD_DEV = 0.05

def main():

    numAlchs, topLeftBounds, bottomRightBounds = takeInput()
    numAlchsRemaining = numAlchs
    Done = False
    while not Done:
        try:
            alchingLoop(numAlchs, numAlchsRemaining, topLeftBounds, bottomRightBounds)
            print("Done!, Alched about " + numAlchs + " items")
        except KeyboardInterrupt:
            print("Done")
        except pyautogui.FailSafeException:  # move to top left corner
            cls()
            print("\r", end='', flush=True)
            input("Execution Paused, Press ENTER to resume")

def alchingLoop(numAlchs, numAlchsRemaining, topLeftBounds, bottomRightBounds):
    while numAlchsRemaining > 0:
        if not isCursorOnAlchBounds(topLeftBounds, bottomRightBounds):
            boundsWarningMsgBase = "\rOut of alching bounds!, moving mouse in "
            countdown = 10
            while countdown > 0:
                boundsWarningMsg = boundsWarningMsgBase + str(countdown) + "s"
                print(boundsWarningMsg, end='', flush=True)
                countdown -= 1
                time.sleep(1)
            moveCursorBackInBounds(topLeftBounds, bottomRightBounds)
            print("\r", end='', flush=True)
        else:
            numAlchsRemaining = castAlch(numAlchsRemaining, numAlchs)
    print("Done!, Alched about " + numAlchs + " items")


def isCursorOnAlchBounds(topLeftBounds, bottomRightBounds):
    currPos = pyautogui.position()
    temp = (currPos[0] > topLeftBounds[0] and currPos[0] < bottomRightBounds[0] and currPos[1] > topLeftBounds[1] and currPos[1] < bottomRightBounds[1])
    return temp

def castAlch(numAlchsRemaining, numAlchs):
    pyautogui.click()
    pyautogui.PAUSE = numpy.random.normal(0.35, 0.05)
    pyautogui.click()
    numAlchsRemaining -= 1
    numAlchsRemainingStr = "\r"+str(numAlchsRemaining) + " of " + str(numAlchs) + " alchs remaining."
    print(numAlchsRemainingStr, end='', flush=True)
    setNextPauseIntervalBetweenAlchs()
    return numAlchsRemaining


def takeInput():
    numAlchs = int(input("1.) enter number of alchs: "))
    input("2.) place cursor on approximate TOP LEFT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    topLeftCoordinates = pyautogui.position()
    print("selected top left: ", str(topLeftCoordinates))
    input("3.) place cursor on approximate BOTTOM RIGHT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    bottomRightCoordinates = pyautogui.position()
    print("selected bottom right: ", str(bottomRightCoordinates))
    input("4.) place cursor on alch icon then press ENTER")
    cls()
    return (numAlchs, topLeftCoordinates, bottomRightCoordinates)


def setNextPauseIntervalBetweenAlchs():
    pyautogui.PAUSE = numpy.random.normal(GAME_TICK_INTERVAL*4.5, 0.45)

def moveCursorBackInBounds(topLeftBounds, bottomRightBounds):
    #find X and Y range within bounds
    minX = topLeftBounds[0]
    maxX = bottomRightBounds[0]
    minY = topLeftBounds[1]
    maxY = bottomRightBounds[1]
    #generate coordinates between maxX, minX, maxY, minY and move there
    randX = random.randint(minX,maxX)
    randY = random.randint(minY,maxY)
    pyautogui.moveTo(randX, randY)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()




