#!/bin/bash

# Wait for X server to be ready (screen is available)
echo "Waiting for X server to be ready..."
while ! xset q &>/dev/null; do
    sleep 1
done
echo "X server is ready."

# Setup apps as executables.
echo "Setting apps as executables..."
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/driver/driver.x86_64
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/flappyTurd/flappyTurd.x86_64
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/schoolCountdown/schoolCountdown.x86_64
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/oranyth/oranyth.x86_64

# Start the driver using box64.
echo "Starting the driver with Box64..."
/usr/local/bin/box64 /home/andrew/Andrew-Arcade/software/apps/driver/driver.x86_64
