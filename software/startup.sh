#!/bin/bash

# Automatically find and make all .x86_64 files in apps/ executable.
find /home/$USER/Andrew-Arcade/software/apps/ -type f -name "*.x86_64" -exec chmod +x {} \;

# Start the driver using box64.
box64 /home/$USER/Andrew-Arcade/software/apps/driver/driver.x86_64