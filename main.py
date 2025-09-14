import keyboard
import subprocess
import datetime
from termcolor import colored

# Define the script to toggle
script_path = '.\skyfish.py'

# Define the key combination to toggle the script
toggle_key = 'ctrl+q'

# Get current date and time
def get_current_time():
    return datetime.datetime.now()

# Initialize the toggle state and running process variables
toggle_state = True
running_process = None
print(colored("====== SKYCK Espresso Machine ======\n", 'magenta'))
print(colored("====== Press CTRL+Q to toggle ======\n", 'magenta'))
# Define the function to execute the script
def execute_script():
    global toggle_state, running_process
    if toggle_state:
        running_process = subprocess.Popen(['python', script_path])
        toggle_state = False
        print(colored(f"[{get_current_time().strftime('%H:%M:%S')}] The Espresso Machine has been turned ON.\n", 'green'))
    else:
        if running_process is not None:
            running_process.terminate()
        toggle_state = True
        print(colored(f"[{get_current_time().strftime('%H:%M:%S')}] The Espresso Machine has been turned OFF.\n", 'red'))

# Register the keyboard event listener
keyboard.add_hotkey(toggle_key, execute_script)

# Start the keyboard event listener loop
keyboard.wait()
