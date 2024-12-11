This is what is actually going to be running on the Raspberry Pi 5. This will be running the games and stuff.

# Startup.sh

chmod +x startup.sh


### Make it run at startup.

Run:
- $ crontab -e

Type this into the crontab to make the script run at startup.
- @reboot  home/${user}/Andrew-Arcade/software/startup.sh
> Adjust the path if you have something different.


# PLAN

need to make a unity package with functions to help developers make their games work