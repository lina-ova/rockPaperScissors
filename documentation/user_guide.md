
# Rock, Paper, Scissors Game: User Guide

## Introduction
Welcome to the Rock, Paper, Scissors game! This guide will take you through the steps to download, install, and play the game.

## Table of Contents
1. [Downloading from GitHub](#downloading-from-github)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Interface Overview](#game-interface-overview)

---

### 1. Downloading from GitHub <a name="downloading-from-github"></a>
Follow these steps to download the game from GitHub:

- Navigate to the GitHub repository link where the game is hosted.
- On the main page of the repository, find and click the green button labeled **"Code"**.
- From the dropdown menu, select **"Download ZIP"**.
- Save the ZIP file to a location on your computer and extract its contents to your desired directory.

---

### 2. Installation <a name="installation"></a>
Before you run the game, make sure you have Python installed.

Next, you need to install the required libraries. In this game, we're using `tkinter` for the GUI and `PIL` from the `Pillow` library for image processing:

- Open your terminal or command prompt.
- Navigate to the directory where you extracted the game files.
- Run the following command to install the required libraries:
   ```
   pip install Pillow
   ```

---

### 3. How to Play <a name="how-to-play"></a>
- Navigate to the directory where you extracted the game files.
- Double-click on the game's Python file (app.py) to run it, or from the terminal, type:
   ```
   python app.py
   ```
- Once the game interface opens, you will see buttons labeled **ROCK**, **PAPER**, and **SCISSORS**.

- Choose your move by clicking one of these buttons.
- The game will display your choice and the computer's choice side by side.
- A message will be displayed below indicating whether you won, lost, or it's a tie.

---

### 4. Game Interface Overview <a name="game-interface-overview"></a>
- **User and Computer Choices**: The choices of both the user and computer are displayed as images in the middle of the screen.
- **Scores**: The scores for the user and computer are displayed above their respective choices.
- **Indicators**: Labels indicating 'USER' and 'COMPUTER' are displayed above the scores.
- **Result Message**: After each round, a message is displayed in the center, indicating the outcome of that round.
- **Buttons**: The ROCK, PAPER, and SCISSORS buttons are located at the bottom for the user to make their choice.

---

## Conclusion
Now you're all set to play the Rock, Paper, Scissors game! Enjoy the challenge against the computer and try to score as high as you can.

--- 
