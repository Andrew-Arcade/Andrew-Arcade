# Auto Starting Driver App

This guide explains how to set up and run the script.

---

## Startup Script: `startup.sh`

This script will handle launching the games and related software.

---

### How to Make the Script Auto Start

1. **Open the file for editing:**

   ```bash
   nano ~/.profile
   ```

2. **Add the path to the script at the end of the file:**

   ```bash
   /home/{username}/Andrew-Arcade/software/startup.sh &
   ```
   > Replace `{username}` with your actual username or adjust the path as needed.

   - The `&` ensures the script runs in the background, so it doesn’t block further startup processes.

3. **Save and exit:**
   - Use `Ctrl+O` to write changes.
   - Press `Enter` to confirm the file name.
   - Use `Ctrl+X` to exit the editor.

---

### Applying Changes

The `~/.profile` file is loaded only for login shells. To apply the changes immediately without logging out and back in, run:

```bash
source ~/.profile
```

---

### Testing the Setup

Reboot the system to ensure the script runs as expected:

```bash
sudo reboot
```