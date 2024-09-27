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

def calibrate(val):
    scaled_val = (val - 50000) / 127
    
    adjuested_val = scaled_val
    if scaled_val < 0:
        adjuested_val = int(scaled_val * 0.31282051282)

    final_val = adjuested_val * 1.04098360656

    return int(final_val)

while True:
    scaled_x = calibrate(ax.value)
    scaled_y = calibrate(ay.value)

    print(f"X0: {raw_x:+10.5f} Y0: {raw_y:+10.5f} X1: {scaled_x:+10.5f} Y1: {scaled_y:+10.5f}")
    
    # Small delay to avoid flooding the output
    time.sleep(0.05)
