import pyautogui

while True:
    # Take a screenshot and save it
    image = pyautogui.screenshot(region=(bbox))

    # Wait for 10 seconds
    time.sleep(1)