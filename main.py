import pyautogui
import numpy
pyautogui.PAUSE = 1
GAME_TICK_INTERVAL = 0.603
print(pyautogui.size())



def main():
    numAlchs, topLeftBounds, bottomRightBounds = takeInput()
    topRightBounds = (bottomRightBounds[0], topLeftBounds[1])
    bottomLeftBounds = (topLeftBounds[0], bottomRightBounds[1])
    

    try:
        while numAlchs > 0:
            if not checkIfCursorNotOnAlch:
                pass #TODO: set cursor into position   
            pyautogui.click()
            numAlchs -= 1
            setNextPauseInterval()
            

    except KeyboardInterrupt:
        print("/nDone")

def checkIfCursorNotOnAlch(topLeftBounds, bottomRightBounds):
    currPos = pyautogui.position()
    return(currPos[0] > topLeftBounds[0] and currPos[0] < bottomRightBounds[0] and currPos[1] > topLeftBounds[1] and currPos[1] < bottomRightBounds[1])

def takeInput():
    numAlchs = input("1.) enter number of alchs: ")
    topLeftCoordinates = input("2.) place cursor on approximate TOP LEFT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    bottomRightCoordinates = input("3.) place cursor on approximate BOTTOM RIGHT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    return (numAlchs, topLeftCoordinates, bottomRightCoordinates)


def setNextPauseInterval():
    pyautogui.PAUSE = numpy.random.normal(GAME_TICK_INTERVAL*5, 0.5)
    print(pyautogui.PAUSE)

if __name__ == "__main__":
    main()




