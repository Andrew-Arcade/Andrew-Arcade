import board
import digitalio
import analogio
import usb_hid
import time
from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

button_pins = (board.GP15, board.GP16,)
gamepad_buttons = (1, 2,) # Up to 16 buttons allowed I think
buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

ax = analogio.AnalogIn(board.A0)
ay = analogio.AnalogIn(board.A1)

# X_CENTER = 49711
# Y_CENTER = 51030
# X_MIN = 6705
# Y_MIN = 65535
# X_MAX = 65535
# Y_MAX = 7953

def debounce():
    time.sleep(0.01)

# def remap(value, centerStart, minStart, maxStart, centerEnd, minEnd, maxEnd):
#     if value >= centerStart:
#         precent = abs(value - maxStart) / abs(centerStart - maxStart)
#         newValue = centerEnd + (abs(centerEnd - maxStart) * percent)
#         return newValue
#     elif value <= centerStart:
#         percent = abs(value - minStart) / abs(minStart - centerEnd)
#         newValue = minEnd + (abs(minEnd - centerEnd) * percent)
#         return newValue
#     else:
#         return centerEnd
#     percent = abs(value - minStart) / abs(maxStart - minStart)
#     newValue = minEnd + abs(maxEnd - minEnd) * percent
#     return int(newValue)

def scale(value):
    return int((value - 32768) / 256)  # Converts 0-65535 range to -127 to 127

while True:
    # x_val = remap(ax.value, X_CENTER, X_MIN, X_MAX, 0, -127, 127) # with remaping
    # y_val = remap(ay.value, Y_CENTER, Y_MIN, Y_MAX, 0, -127, 127) # with remaping
    x_val = scale(ax.value) - 53
    y_val = scale(ay.value) - 56
    gp.move_joysticks(x=x_val, y=y_val)

    print(f"Joystick X: {x_val:+10.5f}, Y: {y_val:+10.5f}")

    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            # print(f"Button {gamepad_button_num}: Released")
        else:
            gp.press_buttons(gamepad_button_num)
            # print(f"Button {gamepad_button_num}: Pressed")

    debounce()
