import pyautogui
import cv2
import numpy as np
import keyboard
import time

NEXT_REGION = (1677, 992, 217, 55)
SKIP_REGION = (1800, 16, 87, 53)

def capture_screen(region):
    screenshot = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

def detect_object(screenshot, templates):
    if not templates:
        print("❌ Error: No template images loaded.")
        return False

    for template in templates:
        if template is None:
            continue

        if screenshot.shape[0] < template.shape[0] or screenshot.shape[1] < template.shape[1]:
            print("❌ Error: Template image is larger than the screenshot region! Skipping this template.")
            continue

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        confidence = np.max(result)
        if confidence > 0.8:
            return True

    return False

def check_skip():
    screen = capture_screen(SKIP_REGION)
    if detect_object(screen, [skip_template]):
        print("Skipping game...")
        keyboard.press_and_release(']')
        time.sleep(0.3)

nextstage_templates = [
    cv2.imread('nextstage.png', 0)
]
skip_template = cv2.imread('skip.png', 0)

if all(t is None for t in nextstage_templates) or skip_template is None:
    print("❌ Error: One or both template images are missing. Check file paths.")
    exit()

while True:
    item_screen = capture_screen(NEXT_REGION)

    is_next = detect_object(item_screen, nextstage_templates)
    is_skip = detect_object(item_screen, [skip_template])

    print(f"Next: {is_next}, Skip: {is_skip}")

    if is_next:
        print("Pressing T")
        keyboard.press_and_release('t')

    check_skip()

    time.sleep(4)
