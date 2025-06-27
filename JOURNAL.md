---
title: "Raspberry Pi Voice Assistant"
author: "Tim Weng"
description: "Raspberry Pi voice assistant that is like Alexa or Siri."
created_at: "2025-06-23"
---
Day 1 (June 27):

11:12

Goals:
I want to make a voice assistant like Siri or Alexa. 
I want to learn how this type of stuff works. I'm new to this, so this is going to be rough.
Also I plan on using ChatGPT and YouTube for help.

Parts: 
Raspberry Pi 4
Micro SD (16GB)
USB Microphone
Speaker (3.5mm or Bluetooth)
Case (for carrying; plan on designing it)

I guess the first thing to do is to set up the Raspberry Pi so that I can upload the OS onto it.
I plan to use Python primarily and utilize an open-source API for voice recognition, and possibly add an AI voice assistant.

11:22

First on the Raspberry Pi I need to install/check Python, so using the terminal: python3 --version, if version isn't 3.6+ O need to upgrade: sudo apt update
sudo apt install python3 python3-pip. The reason why I need 3.6+ is because these versions are needed to use the libraries for the project. 

11:28

I finished installing Python, and now I need to install the audio libraries.
While trying to install I ran into an error saying: externally managed environment.

11:32

The error is because the Raspberry Pi OS is preventing the installation of the audio libraries.
The plan is to make a local folder and run it inside a Virtual Environmenmt.

11:34 

Finished installing the libraries. To activate the VM I need to run the command: source my_voice_env/bin/activate
