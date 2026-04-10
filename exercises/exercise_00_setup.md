# Exercise 0 — Getting Set Up

This guide walks you through everything before you write your first line of Python. Take it one step at a time — your volunteers are here to help!

---

## Step 1 — Get the workshop folder

Your volunteer will share either a **link** or a **USB stick**.

### From a link

1. Go to **tinyurl.com/python-walthamstow-workshop**
2. Click the green **Code** button near the top right
3. Click **Download ZIP**
4. The file downloads to your Downloads folder

### From a USB stick

Copy the `.zip` file from the USB stick to your Desktop (or anywhere easy to find).

### Unzip it

**Mac**
1. Double-click the `.zip` file
2. A folder appears next to it — that's your workshop folder

**Windows**
1. Right-click the `.zip` file
2. Choose **Extract All…**, then click **Extract**
3. A folder appears — that's your workshop folder

The folder will be called something like **`python-music-workshop`**. Put it somewhere easy to find, like your Desktop.

---

## Step 2 — Run the setup script

The setup script checks that everything is working. Here's how to run it:

### On a Mac

1. **Open Terminal**
   Press `Cmd + Space` to open Spotlight, type **Terminal**, and press Enter.
   A window with a text prompt appears — that's the terminal.

2. **Type `bash ` followed by a space** (don't press Enter yet)

3. **Drag the setup file into the Terminal window**
   Open your workshop folder → open the `setup` folder → find `setup.command`.
   Drag that file into the Terminal window. The file path appears automatically.

4. **Press Enter**
   The script runs and prints its results.

### On a Windows PC

1. **Open the `setup` folder**
   Go into your workshop folder, then open the `setup` folder.

2. **Open a Command Prompt here**
   Click once in the **address bar** at the top of the window (it shows the folder path).
   Type `cmd` and press Enter. A black Command Prompt window opens in the right place.

3. **Type `setup.bat` and press Enter**
   The script runs and prints its results.

---

## Step 3 — Read the output

You should see something like this:

```
[ OK ] Python 3.12.3 (bundled)
[ OK ] Loaded 9237 songs.

*** ALL DONE — YOU'RE GOOD TO GO! ***
```

Both lines should say `[ OK ]`. If you see that — great, move on to Step 4!

If anything shows `[FAIL]`, the script will tell you what to do next. Read the **FIX** instructions, or show the window to your volunteer — they'll help you sort it out.

---

## Step 4 — Open VS Code

VS Code is the program you'll write your Python code in.

1. Open **VS Code** (it may already be in your taskbar or Applications folder)
2. Go to **File → Open Folder…**
3. Find your workshop folder (e.g. on the Desktop), click it once to select it, then click **Open**
4. You should see the `exercises` folder appear in the left panel

> **First time on Mac?** VS Code may ask "Do you trust the authors of the files in this folder?" — click **Yes, I trust the authors**.

---

## Step 5 — Open the built-in terminal

VS Code has its own terminal built in — you'll use it to run your Python exercises.

Press `` Ctrl+` `` (that's the backtick key — top-left of your keyboard, to the left of the `1` key).

A panel opens at the bottom of the screen with a text prompt. You're in the right folder already.

Type this and press Enter:

```
python3 exercises/exercise_00_setup_check.py
```

You should see:

```
Everything is set up correctly — you're ready to go!
```

If you see that — you're done! Start on Exercise 1.

> **Windows tip:** if `python3` doesn't work, try `python` instead.

---

## Bonus — the Data Explorer

There's a webpage that lets you browse 9,000+ real songs and see exactly how to use any of them in your code.

**Mac:** in Terminal, type `bash ` and drag `explore.command` into the window, then press Enter.
**Windows:** open the `setup` folder, click the address bar, type `cmd`, press Enter, then type `explore.bat`.

Press Enter in the terminal window (or close it) when you're done.

---

## Quick reference

| What | How |
|------|-----|
| Run setup | Mac: `bash ` + drag `setup/setup.command` into Terminal · Windows: open `setup/` in Explorer, type `cmd` in address bar, run `setup.bat` |
| Open the terminal in VS Code | `` Ctrl+` `` (backtick key) |
| Run an exercise | `python3 exercises/exercise_01_variables_and_strings.py` |
| Open the data explorer | Mac: `bash ` + drag `setup/explore.command` · Windows: same trick with `explore.bat` |
