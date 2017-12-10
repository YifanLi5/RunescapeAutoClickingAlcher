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

#TODO: moving cursor back sometimesis in a spot that can select cast alch but not cast it on an item (find hitboxes for both)

def main():

    num_alchs, top_left_bounds, bottom_right_bounds = takeInput()
    num_alchs_remaining = num_alchs
    done = False
    while not done:
        try:
            done, num_alchs_remaining = alchingLoop(num_alchs, num_alchs_remaining, top_left_bounds, bottom_right_bounds)
        except KeyboardInterrupt:
            print("Done")
        except pyautogui.FailSafeException:  # move to top left corner
            cls()
            print("\r", end='', flush=True)
            input("Execution Paused, Press ENTER to resume")
    exit(0)

def alchingLoop(numAlchs, numAlchsRemaining, topLeftBounds, bottomRightBounds):
    pauseAfterXAlchs = random.randint(750, 1500)
    while numAlchsRemaining > 0:
        if not isCursorOnAlchBounds(topLeftBounds, bottomRightBounds):
            boundsWarningMsgBase = "\rOut of alching bounds! Moving mouse in "
            countdown = 10
            while countdown > 0:
                boundsWarningMsg = boundsWarningMsgBase + str(countdown) + "s"
                print(boundsWarningMsg, end='', flush=True)
                countdown -= 1
                time.sleep(1)
                if checkIfMouseInPauseRegion():
                    raise pyautogui.FailSafeException
            moveCursorBackInBounds(topLeftBounds, bottomRightBounds)
            cls()
            print("\r", end='', flush=True)
        else:
            randomPauseIfNeeded(pauseAfterXAlchs)
            numAlchsRemaining = castAlch(numAlchsRemaining, numAlchs)
    print("Done!, Alched " + str(numAlchs) + " items")
    return True, numAlchsRemaining

def randomPauseIfNeeded(pauseAfterXAlchs):
    pauseAfterXAlchs -= 1
    if pauseAfterXAlchs <= 0:
        pause_time = numpy.random.normal(15, 3)
        print("\r", end='', flush=True)
        print("pausing for: " + str(pause_time), end='', flush=True)
        time.sleep(pause_time)
        pauseAfterXAlchs = random.randint(750, 1500)
    return pauseAfterXAlchs

def checkIfMouseInPauseRegion():
    pyautogui.PAUSE = 0.2
    x, y = pyautogui.position()
    return x < 100 and y < 100

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




