import pyautogui
import numpy
import os
pyautogui.PAUSE = 1
GAME_TICK_INTERVAL = 0.603
print(pyautogui.size())



def main():
    numAlchs, topLeftBounds, bottomRightBounds = takeInput()
    try:
        while numAlchs > 0:
            if not isCursorOnAlch(topLeftBounds, bottomRightBounds):
                print("out of bounds")
                pass #TODO: set cursor into position   
            pyautogui.click()
            pyautogui.PAUSE = numpy.random.normal(0.35, 0.05)
            pyautogui.click()
            numAlchs -= 1
            setNextPauseInterval()
            

    except KeyboardInterrupt:
        print("Done")

def isCursorOnAlch(topLeftBounds, bottomRightBounds):
    currPos = pyautogui.position()
    temp = (currPos[0] > topLeftBounds[0] and currPos[0] < bottomRightBounds[0] and currPos[1] > topLeftBounds[1] and currPos[1] < bottomRightBounds[1])
    return temp

def takeInput():
    numAlchs = int(input("1.) enter number of alchs: "))
    input("2.) place cursor on approximate TOP LEFT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    topLeftCoordinates = pyautogui.position()
    print("top left: ", str(topLeftCoordinates))
    input("3.) place cursor on approximate BOTTOM RIGHT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    bottomRightCoordinates = pyautogui.position()
    print("bottom right: ", str(bottomRightCoordinates))
    input("4.) place cursor on alch icon then press ENTER")
    cls()
    return (numAlchs, topLeftCoordinates, bottomRightCoordinates)


def setNextPauseInterval():
    pyautogui.PAUSE = numpy.random.normal(GAME_TICK_INTERVAL*4.5, 0.25)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    

if __name__ == "__main__":
    main()




