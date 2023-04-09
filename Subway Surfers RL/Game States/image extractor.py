import pyautogui
import time
import datetime

bbox = 620,0,650,1200
while True:
    # take current datetime and set it to file name
    now = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")

    #path to store the screenshots
    path = r"C:\Users\Zaid Salahuddin\Documents\Snek Schizms\Subway Surfers RL\Game States\screenshots\\"

    #takes the path and now to name the screenshot
    filename = path + now + '.png'
    #convert into path object
    print("file name is:", filename,' File Type:', type(filename))

    # Take a screenshot and save it
    pyautogui.screenshot(filename, region=(bbox))


    # Wait for 10 seconds
    time.sleep(2)