import board
import digitalio
import analogio
import time

# Setup onboard LED to indicate if the script is running
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Define analog inputs for joystick
ax = analogio.AnalogIn(board.A0)  # X-axis
ay = analogio.AnalogIn(board.A1)  # Y-axis

def scale(value):
    return int((value - 32768) / 256)  # Converts 0-65535 range to -127 to 127

def calibrate(value, center):
    if value > center:
        height = 127
    elif value < center:
        height = -127
    else:
        return center

    percent = abs(center - value) / abs(height - center)
    new_value = height * percent
    return new_value
         
while True:
    # Read analog values
    raw_x = ax.value
    raw_y = ay.value
    
    # Scale the values
    scaled_x = scale(raw_x)
    scaled_y = scale(raw_y)

    # final_x = calibrate(scaled_x, 61)
    # final_y = calibrate(scaled_y, 67)

    final_x = scaled_x - 53
    final_y = scaled_y - 56
    
    # Print the scaled values with 3 digits before the decimal and 5 decimal places, accounting for the negative sign
    print(f"X0: {scaled_x:+10.5f} Y0: {scaled_y:+10.5f} X1: {final_x:+10.5f} Y1: {final_y:+10.5f}")
    
    # Toggle the onboard LED to show the script is running
    led.value = not led.value
    
    # Small delay to avoid flooding the output
    time.sleep(0.05)
