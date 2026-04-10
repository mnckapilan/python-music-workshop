# Exercise 0 — Getting Set Up

Before you write any Python, you need two things on your laptop:

- **Python** — the language we'll use
- **VS Code** — the program we'll write code in

The setup script checks both for you and opens VS Code when everything is ready.

---

## Step 1 — Run the setup script

Find the file in the **python-music-workshop** folder that matches your laptop.

### On a Mac

1. Open the **python-music-workshop** folder in Finder
2. Open the **`setup`** folder, then find the file called **`setup.command`**
3. **Right-click** it and choose **Open** (you must right-click the first time — double-clicking won't work until macOS trusts the file)
4. A terminal window will open and run the checks automatically

### On a Windows PC

1. Open the **python-music-workshop** folder in File Explorer
2. Open the **`setup`** folder, then find the file called **`setup.bat`**
3. Double-click it
4. A command prompt window will open and run the checks automatically

---

## Step 2 — Read the output

The script prints a result for each check:

```
[ OK ] Python 3.11.4
[ OK ] VS Code 1.89.0
[ OK ] Loaded 9237 songs.

All 3 checks passed — you're ready to go!
Opening VS Code...
```

If everything passes, VS Code opens automatically and you're done — skip to Step 3.

If something fails, you'll see something like:

```
[FAIL] Python — not found

  ISSUE 1: Python 3 is not installed.
  FIX 1:   Go to https://www.python.org/downloads/ and install Python 3.11.
```

Follow the **FIX** instructions for each issue, then re-run the setup script.

> If you're stuck, show this window to your volunteer or teaching assistant — the error messages are written so they know exactly what to fix.

---

## Step 3 — Open your first exercise

Once VS Code is open:

1. In the left panel, click the **`exercises`** folder to expand it
2. Click **`exercise_01_variables_and_strings.py`**
3. You'll see the file open on the right — have a read through it

To **run** the file, open a terminal in VS Code:
- Mac: press `` Ctrl+` `` (the backtick key, top-left of your keyboard)
- Windows: press `` Ctrl+` ``

Then type:

```
python3 exercises/exercise_01_variables_and_strings.py
```

(On Windows, try `python` instead of `python3` if that doesn't work.)

You should see some output printed in the terminal. If you do — you're ready to start coding!

---

## Bonus — the Data Explorer

There's a webpage that lets you browse the full music library (9,000+ real songs) and shows you how to access each one in Python.

To open it, type this in the VS Code terminal:

```
python3 data/explorer.py
```

It will open in your browser automatically.

---

## Quick Reference

| Task | Command |
|------|---------|
| Run an exercise | `python3 exercises/exercise_01_variables_and_strings.py` |
| Open the data explorer | `python3 data/explorer.py` |
| Re-run setup checks | double-click `setup/setup.command` (Mac) or `setup/setup.bat` (Windows) |
