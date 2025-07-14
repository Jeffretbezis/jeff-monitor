import time
from pynput import keyboard, mouse

print("Jeffmonitor v1, by jeffretbezis")
print("All logs are kept client sided and deleted after closing the console.\n")

current_line = []
mouse_down = False

def on_press(key):
    global current_line
    try:
        if key.char == ' ':
            if current_line:
                print(','.join(current_line))
                current_line = []
        else:
            current_line.append(key.char)
    except AttributeError:
        pass

def on_click(x, y, button, pressed):
    global mouse_down, current_line
    mouse_down = pressed
    if pressed:
        if current_line:
            print(','.join(current_line))
            current_line = []
        print(f"Click at ({x}, {y})")

keyboard.Listener(on_press=on_press).start()
mouse.Listener(on_click=on_click).start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
