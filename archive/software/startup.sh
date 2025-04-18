#!/bin/bash

# Setup doom files.


# Setup apps as executables.
chmod +x /home/$USER/Andrew-Arcade/software/apps/driver/driver.x86_64
chmod +x /home/$USER/Andrew-Arcade/software/apps/flappyTurd/flappyTurd.x86_64
chmod +x /home/$USER/Andrew-Arcade/software/apps/schoolCountdown/schoolCountdown.x86_64
chmod +x /home/$USER/Andrew-Arcade/software/apps/oranyth/oranyth.x86_64

# Start the driver using box64.
box64 /home/$USER/Andrew-Arcade/software/apps/driver/driver.x86_64
