> [!NOTE]
> You can automate this process by running [setup_autostart.sh](setup_autostart.sh).

# Auto Starting Driver App

This guide explains how to set up and run the script automatically when logging into the Raspberry Pi OS desktop.

---

## Startup Script: `startup.sh`

This script will handle launching the games and related software.

---

## How to Make the Script Auto Start (GUI Method)

### Step 1: Create the Autostart Directory  
Ensure the autostart directory exists by running:

```bash
mkdir -p ~/.config/autostart
```

---

### Step 2: Create the Startup Entry  
Create a new `.desktop` file:

```bash
nano ~/.config/autostart/start-driver.desktop
```

Then, add the following content:

```ini
[Desktop Entry]
Type=Application
Name=Start Driver
Exec=/home/{username}/Andrew-Arcade/software/startup.sh
StartupNotify=false
Terminal=false
```

> Replace `{username}` with your actual username.

---

### Step 3: Make the Script Executable  
Ensure the script has the correct permissions:

```bash
chmod +x /home/{username}/Andrew-Arcade/software/startup.sh
```

---

### Step 4: Restart to Apply Changes  
Reboot your Raspberry Pi to test the setup:

```bash
sudo reboot
```

Your script should now start automatically when you log into the **Raspberry Pi OS desktop**. 🎉