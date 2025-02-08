#!/bin/bash

# Setup apps as executables.
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/driver/driver.x86_64
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/flappyTurd/flappyTurd.x86_64
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/schoolCountdown/schoolCountdown.x86_64
/usr/bin/chmod +x /home/andrew/Andrew-Arcade/software/apps/oranyth/oranyth.x86_64

# Start the driver using box64.
/usr/local/bin/box64 /home/andrew/Andrew-Arcade/software/apps/driver/driver.x86_64
