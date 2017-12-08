import pyautogui
import numpy
pyautogui.PAUSE = 1
GAME_TICK_INTERVAL = 0.603
print(pyautogui.size())



def main():
    numAlchs, topLeftBounds, bottomRightBounds = takeInput()
    print numAlchs, topLeftBounds, bottomRightBounds
    try:
        while numAlchs > 0:
            if not isCursorOnAlch(topLeftBounds, bottomRightBounds):
                print("out of bounds")
                pass #TODO: set cursor into position   
            pyautogui.click()
            numAlchs -= 1
            setNextPauseInterval()
            

    except KeyboardInterrupt:
        print("/nDone")

def isCursorOnAlch(topLeftBounds, bottomRightBounds):
    currPos = pyautogui.position()
    temp = (currPos[0] > topLeftBounds[0] and currPos[0] < bottomRightBounds[0] and currPos[1] > topLeftBounds[1] and currPos[1] < bottomRightBounds[1])
    print temp
    return temp

def takeInput():
    numAlchs = input("1.) enter number of alchs: ")
    raw_input("2.) place cursor on approximate TOP LEFT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    topLeftCoordinates = pyautogui.position()
    print("top left: ", str(topLeftCoordinates))
    raw_input("3.) place cursor on approximate BOTTOM RIGHT of alch icon\nmake sure that you can still cast high alch then press ENTER")
    bottomRightCoordinates = pyautogui.position()
    print("bottom right: ", str(bottomRightCoordinates))
    return (numAlchs, topLeftCoordinates, bottomRightCoordinates)


def setNextPauseInterval():
    pyautogui.PAUSE = numpy.random.normal(GAME_TICK_INTERVAL*5, 0.5)
    

if __name__ == "__main__":
    main()




