# Espresso Machine - Fishing Automation Scripts

A collection of Python scripts designed to automate fishing-related minigames. These scripts act as "bots" that use different techniques to perform repetitive in-game tasks, freeing up the player. The project is nicknamed "Espresso Machine" as it handles the "grind".

The repository contains two main bots:
1.  **The Skyfish Bot:** An advanced bot that uses real-time image and color recognition to play a complex fishing minigame.
2.  **The Legalfish Bot:** A simpler bot that uses Optical Character Recognition (OCR) to detect when a fish has bitten.

---

## Bots Overview 🤖

### 1. Skyfish Bot (`skyfish.py`)
This bot is designed for a dynamic minigame where the player must keep an icon within a specific zone. It works by constantly analyzing a vertical region of the screen.

* **How it Works:**
    * It identifies the vertical position of two key colors: a "bad" green zone and a yellow "fish" indicator.
    * If the fish indicator is detected *above* the green zone, the script simulates pressing the 'up' arrow key to correct its position.
    * It also monitors a specific pixel on the screen for a blue color, indicating a successful catch, at which point it presses 'e' and clicks to re-apply bait for the next round.

### 2. Legalfish Bot (`legalfish.py`)
This bot is for a more straightforward waiting game. It automates the process of waiting for a fish to bite and then reeling it in.

* **How it Works:**
    * The script repeatedly takes a screenshot of a specific area on the screen where a notification appears.
    * It uses **Optical Character Recognition (OCR)** via Tesseract to read the text in that area.
    * If it reads the text "THE FISH BIT!", it simulates a mouse click to catch the fish and then automatically recasts the line.

---

## Technologies Used 🛠️

* **Language:** Python
* **Automation/Control:** `pyautogui` (for mouse control and key presses), `keyboard` (for global hotkey listening)
* **Image Recognition:** `Pillow` (PIL) for screen capturing and pixel analysis
* **OCR:** `pytesseract` (a Python wrapper for Google's Tesseract-OCR Engine)
* **Terminal UI:** `termcolor` for colored console output

---

## How to Use ▶️

Each bot is launched using its corresponding `main` script, which sets up a global hotkey to start and stop the automation.

### 1. Prerequisites
* **Install Python Libraries:**
    ```bash
    pip install keyboard pyautogui Pillow termcolor pytesseract
    ```
* **Install Tesseract-OCR:** You must install Google's Tesseract OCR engine on your system. The scripts are configured for a Windows installation path (`C:\Program Files\Tesseract-OCR\tesseract.exe`). You may need to adjust this path in the `.py` files if your installation is different.

### 2. Running a Bot

To run a bot, execute its main script from your terminal.

* **To run the Skyfish Bot:**
    ```bash
    python main.py
    ```
* **To run the Legalfish Bot:**
    ```bash
    python mainlegal.py
    ```

Once the script is running, press **`CTRL + Q`** to toggle the bot ON or OFF. You will see a confirmation message in the terminal each time you toggle it.

---

## ⚠️ Disclaimer

These scripts are highly dependent on screen resolution, in-game UI element positions, and specific colors. The coordinates and RGB values are hard-coded for a particular setup.

If you wish to use these on your own system, you will likely need to:
* Update the screen coordinates in `skyfish.py` (e.g., `success_position`, `bait_position`, `region`) and `legalfish.py` (the `region` for the screenshot).
* Adjust the RGB color values and tolerance in `skyfish.py` to match your game's visuals.