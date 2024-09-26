#include <Adafruit_TinyUSB.h>  // Correct include for TinyUSB support

// Define button pins (use GPIO pin numbers)
const int buttonPin1 = 15;  // GP15
const int buttonPin2 = 14;  // GP14

void setup() {
  // Initialize the button pins as input with internal pull-up resistors
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);

  // Start the TinyUSB for HID (keyboard) functionality
  TinyUSB_Device_Init(0);
  tud_hid_keyboard_report(0, 0, NULL);  // Release all keys
}

void loop() {
  uint8_t keycode[6] = { 0 }; // Array to store keypresses

  // Check if button 1 is pressed
  if (digitalRead(buttonPin1) == LOW) {
    keycode[0] = HID_KEY_A;  // 'A' key
  }

  // Check if button 2 is pressed
  if (digitalRead(buttonPin2) == LOW) {
    keycode[1] = HID_KEY_B;  // 'B' key
  }

  // Send the keycode (report) to the host if any key is pressed
  tud_hid_keyboard_report(0, 0, keycode);

  // Small delay to avoid bouncing
  delay(10);
}

void end() {
  tud_hid_keyboard_report(0, 0, NULL);  // Release all keys
}
