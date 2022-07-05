
# FFF Discord Bot

A bot that will help you to make a FFF round perfect for everyone who can connect to Discord

## How to Install

1. Download python, you can download python in [this link](https://www.python.org/downloads/). Remeber to add python into PATH or you will have some problem with into

2. Install nextcord (discord.py is outdated lol)
**Use these command line to install**


    # Linux/macOS
    ```
    python3 -m pip install -U nextcord
    ```
    
    # Windows
    ```
    py -3 -m pip install -U nextcord
    ```
3. Creating a bot like you creating a normal bot
**You must enable PRESENCE INTENT, SERVER MEMBERS INTENT and MESSAGE CONTENT INTENT so the bot can work**

4. Run the bot and try to learn it lol
## How to use

The prefix of the bot is t! but you can change if you know how to code

* t!start: This will start the round, annouce player to enter their answer, after few second (20 second is the default) it will lock and stop player from answer
* t!add [player]: This will add player into the list
* t!remove [player]: This will remove player out of the list
* t!test: This will check that if the bot is working properly by sending a message
* t!timeleft: check how much time is left (Is not 100% correct but i'm too lazy to fix)
* t!save: Save all of the player so you don't need to add them again
* t!load: Load the data that you save so you can start a new game
* t!answer [answer] (Only for strict mode): import your answer to the bot
## Strict Mode

You can access it by changing the value in config file of the mode to True

This will make your bot only recive correct answer instead of recive all of player's answers

This maybe have alot of error so I'm not suggest you to do it

You need to import your answer first before start the game so the bot and recive only the correct answer

## Before you using

Please give a credit to my work by linking this github page

I don't take money because I make this for WWTBAM community and I'm too young to make money lol