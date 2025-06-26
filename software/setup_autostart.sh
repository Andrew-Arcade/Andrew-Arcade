#!/bin/bash

# Prompt the user for the full path to startup.sh
read -p "Enter the full path to your startup.sh script: " STARTUP_SCRIPT

# Check if the file exists
if [ ! -f "$STARTUP_SCRIPT" ]; then
    echo "Error: $STARTUP_SCRIPT does not exist."
    exit 1
fi

# Get the user's home directory
USER_HOME="$HOME"

# Paths
AUTOSTART_DIR="$USER_HOME/.config/autostart"
DESKTOP_FILE="$AUTOSTART_DIR/start-driver.desktop"

# 1. Create autostart directory if it doesn't exist
mkdir -p "$AUTOSTART_DIR"

# 2. Create the .desktop file
cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=Start Driver
Exec=$STARTUP_SCRIPT
StartupNotify=false
Terminal=false
EOF

# 3. Make the startup script executable
chmod +x "$STARTUP_SCRIPT"

echo "Autostart setup complete. Please reboot to test."