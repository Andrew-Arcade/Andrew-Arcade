# Andrew Arcade

Check out my progress in the [log](LOG.md)!

## About the Project

Custom game console designed to run my Unity games.

Designed on top of the Raspberry Pi 5 running pios.

We use [box64](https://github.com/ptitSeb/box64) to run Unity games on the ARM architecture. 

## Apps

### How to contribute your app

To create your own app, you'll need to submit all the source code (the full Unity project) to the apps repository. You will also need to modify the driver app to include your app (details will be provided later). Once your app is ready for release, submit a pull request (PR) to the apps repository. After your PR is approved, you can build the app and submit a second PR to this main Andrew Arcade repository.

### App file structure

Go to the [software/apps](software/apps) directory and create a new folder. Name the folder after your app using camelCase (no spaces, capitalize the first letter of each new word except for the first one). Then, place your app's build files inside the folder you just created.

### Why maintain a second repository?

Unity projects typically require a large amount of storage, while Raspberry Pi 5 devices often have limited space. As a result, the source code for the apps doesn't need to be stored directly on the device.

### More app information

For additional details about the apps or games, check out the [Andrew Arcade Apps](https://github.com/AndrewCromar/Andrew-Arcade-Apps) repository.