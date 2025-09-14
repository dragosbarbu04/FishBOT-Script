import pyautogui
from PIL import Image

def find_color_in_region(color_rgb, region, tolerance=30):
    # Take a screenshot of the specified region only
    left, top, width, height = region
    screenshot = pyautogui.screenshot(region=region)

    # Convert the screenshot to an image object
    img = screenshot.convert('RGB')
    
    # Initialize to store the highest and lowest y-coordinate for each color found
    min_y = height  # Start with the bottom most part of the region

    # Search for the color within the region
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            # Check if the pixel matches the target color within the given tolerance
            if all(abs(pixel[i] - color_rgb[i]) <= tolerance for i in range(3)):
                # Update min_y if a higher (smaller y value) pixel is found
                if y < min_y:
                    min_y = y
                    break  # Stop searching further down once the first match is found in this column
    if min_y == height:
        return None  # If min_y did not change, color not found
    return min_y

def take_action_based_on_color_position(region):
    # Define the colors
    bad_green_rgb = (112, 200, 93)
    fish_rgb = (255, 246, 0)

    # Find the highest points where each color is found in the region
    bad_green_position = find_color_in_region(bad_green_rgb, region)
    fish_position = find_color_in_region(fish_rgb, region)

    # Check positions and take action if bad green is above fish
    if bad_green_position is not None and fish_position is not None:
        if bad_green_position > fish_position:
            print(f"Fish is above green: Bad Green Y = {bad_green_position}, Fish Y = {fish_position}")
            pyautogui.keyDown('up')
            print("Pressed UP_ARROW since fish is above green.")
        else:
            print("Fish is not above green.")
            pyautogui.keyUp('up')
            pyautogui.sleep(0.5)
    else:
        print("One or both colors not found.")

import pyautogui
from PIL import Image

def color_matches(color1, color2, tolerance=30):
    # Check if the difference between each RGB component is within the tolerance
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def check_color_and_act(success_rgb, success_position, bait_position, tolerance=30):
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to an RGB image
    img = screenshot.convert('RGB')

    # Get the RGB value of the pixel at the success position
    pixel_color = img.getpixel(success_position)

    # Compare the pixel color to the success_rgb with tolerance
    if color_matches(pixel_color, success_rgb, tolerance):
        print(f"Color match at {success_position} within tolerance: {pixel_color}")
        # Press 'e'
        pyautogui.press('e')
        print("Pressed 'e'.")

        # Click at the bait position
        pyautogui.click(bait_position)
        print(f"Clicked at {bait_position}.")
    else:
        print(f"No color match at {success_position}. Found color {pixel_color}, expected {success_rgb} within tolerance.")


# Example usage
tolerance = 45
success_rgb = (0, 157, 255)
success_position = (990, 120)
bait_position = (960, 540)
screen_width, screen_height = pyautogui.size()
left = (screen_width - 100) // 2
top = (screen_height - 380) // 2
width = 50
height = 400
region = (left, top, width, height)

while True:
    take_action_based_on_color_position(region)
    check_color_and_act(success_rgb, success_position, bait_position, tolerance)

