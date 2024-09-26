import board
import digitalio
import analogio
import time

# Setup onboard LED to indicate if the script is running
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Blink the LED 3 times to indicate the script is running
for _ in range(3):
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

# Define analog inputs for joystick
ax = analogio.AnalogIn(board.A0)  # X-axis
ay = analogio.AnalogIn(board.A1)  # Y-axis

# Calibration variables
X_CENTER = 0
Y_CENTER = 0
X_MIN = 0
Y_MIN = 0
X_MAX = 0
Y_MAX = 0

def map_float(x, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def calibrate():
    global X_CENTER, Y_CENTER, X_MIN, Y_MIN, X_MAX, Y_MAX

    print("\n--- Calibrating Joystick ---\n")

    # Step 1: Center Calibration
    print("Step 1: Place the joystick in the center position and wait...")
    time.sleep(2)  # Delay for user to place the joystick
    cal_X = 0
    cal_Y = 0
    for _ in range(100):
        cal_X += ax.value
        cal_Y += ay.value
        time.sleep(0.01)  # Small delay to stabilize readings
    X_CENTER = cal_X // 100
    Y_CENTER = cal_Y // 100
    print(f"Center X: {X_CENTER}, Center Y: {Y_CENTER}")

    # Step 2: Minimum Calibration
    print("\nStep 2: Move the joystick to the bottom-left corner and wait...")
    time.sleep(2)
    X_MIN = ax.value
    Y_MIN = ay.value
    for _ in range(100):
        X_MIN = min(X_MIN, ax.value)
        Y_MIN = min(Y_MIN, ay.value)
        time.sleep(0.01)
    print(f"Min X: {X_MIN}, Min Y: {Y_MIN}")

    # Step 3: Maximum Calibration
    print("\nStep 3: Move the joystick to the top-right corner and wait...")
    time.sleep(2)
    X_MAX = ax.value
    Y_MAX = ay.value
    for _ in range(100):
        X_MAX = max(X_MAX, ax.value)
        Y_MAX = max(Y_MAX, ay.value)
        time.sleep(0.01)
    print(f"Max X: {X_MAX}, Max Y: {Y_MAX}")

    # Output the calibration results
    print("\n--- Calibration Complete ---")
    print(f"Center: ({X_CENTER}, {Y_CENTER}), Min: ({X_MIN}, {Y_MIN}), Max: ({X_MAX}, {Y_MAX})")

# Run the calibration once and end the program
calibrate()
