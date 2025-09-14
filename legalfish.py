import pyautogui
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def catch_fish():
    while True:
        print("Checking for fish...")
        waiting = pyautogui.screenshot(region=(855, 268, 230, 60))
        text = pytesseract.image_to_string(waiting)
        if text.strip() == "THE FISH BIT!":
            pyautogui.click(960, 540)
            print("Fish caught!")
            pyautogui.sleep(2)
            break
        else:
            print("Still waiting")
            pyautogui.sleep(1)

def main():
    pyautogui.sleep(1)
    pyautogui.press("e")

    print("Selecting fish bait")
    pyautogui.click(960, 540)

    print("Waiting for fish to bite")
    pyautogui.sleep(20)

while True:
    main()
    catch_fish()