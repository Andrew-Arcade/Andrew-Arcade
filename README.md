<img src="media/logo/andrew-arcade-logo.png">

Check out my progress in the [journal](JOURNAL.md)!

<!-- ### About Andrew Arcade

Andrew Arcade is a custom game console built with a Raspberry Pi 5 running Linux. Its main purpose is to play Unity games that I have created.

Since the Raspberry Pi 5 uses an ARM processor, Unity games can't be compiled to run on it directly. To solve this, we use a tool called Box64, which lets us run Unity games and apps on the Raspberry Pi by emulating the required architecture.

### Version 2

Version 2 of Andrew Arcade will feature a redesigned case. My goal is to make it more comfortable to use and to improve some of the mounting parts that didn’t work well in the first version. -->

## About the Project

Custom game console designed to run my Unity games.

Designed on top of the Raspberry Pi 5 running pios.

We use [box64](https://github.com/ptitSeb/box64) to run Unity games on the ARM architecture. 

## Driver App

The driver app acts as the game hub, allowing you to choose which game to play. It should be configured to launch automatically at startup to provide a seamless experience.

For detailed steps on how to set up the driver app to auto-start, see [this guide](software/README.md).

## Apps
[Andrew-Arcade-Apps](https://github.com/AndrewCromar/Andrew-Arcade-Apps) (referred to as "apps repository")
> Most up to date information will be in the apps repository eventually.

### How to contribute your app

To create your own app, you'll need to submit all the source code (the full Unity project) to the apps repository. You will also need to modify the driver app to include your app (details will be provided later). Once your app is ready for release, submit a pull request (PR) to the apps repository. After your PR is approved, you can build the app and submit a second PR to this main Andrew Arcade repository.

### App file structure

Go to the [software/apps](software/apps) directory and create a new folder. Name the folder after your app using camelCase (no spaces, capitalize the first letter of each new word except for the first one). Then, place your app's build files inside the folder you just created.

### Why maintain a second repository?

Unity projects typically require a large amount of storage, while Raspberry Pi 5 devices often have limited space. As a result, the source code for the apps doesn't need to be stored directly on the device.

### More app information

For additional details about the apps or games, check out the [Andrew Arcade Apps](https://github.com/AndrewCromar/Andrew-Arcade-Apps) repository.

## Parts

| Name                  | URL                                                                                                    | Notes                                                                                                   |
|-----------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Raspberry Pi 5        | [link](https://www.raspberrypi.com/products/raspberry-pi-5/)                          | Price: $80.                                                                                            |
| Raspberry Pi Pico     | [link](https://www.raspberrypi.com/products/raspberry-pi-pico/)                        | Purchase with headers pre-soldered for easier assembly.                                                 |
| Adafruit HDMI Display | [link](https://www.adafruit.com/product/2232)                                        | Price: $60. <br> Resolution: 800x480 <br> Size: 5 inches.                                              |
| Power Button          | [link](https://www.amazon.com/Momentary-pre-Wiring-Waterproof-Stainless-Normally/dp/B09BKXT1J1/ref=sr_1_21?crid=1UOTGELQWX2QV&qid=1748031298&sprefix=push%2Bbutton%2Caps%2C246&sr=8-21&xpid=hIhX7cwb6-fjm&th=1) | Maximum diameter: 17.3 mm <br> Fitting diameter: 13.0 mm <br> Total height: 21.4 mm <br> Height from button top to narrow section: 8.3 mm. |
| Joysticks             | [link](https://www.adafruit.com/product/512)                                           | Soldering is required for assembly.                                                                    |
| 90 Degree Headers     | [link](https://www.amazon.com/PATIKIL-Header-Single-2-54mm-Plated/dp/B0C81QTKC5?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&gQT=1&th=1) | Used to connect the joysticks to the board.                                                            |
| DAC                   | [link](https://www.digikey.com/en/products/detail/microchip-technology/MCP3008-I-P/319422) | Allows you to connect more than three analog inputs from the joysticks to the Pico.                     |