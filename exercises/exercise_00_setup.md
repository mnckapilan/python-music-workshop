# Exercise 0 — Getting Set Up

Before you write any Python, you need two things on your laptop:

- **Python** — the language we'll use
- **VS Code** — the program we'll write code in

The setup script checks both for you and opens VS Code when everything is ready.

---

## Step 1 — Open the workshop folder

Your volunteer will give you a **.zip file**. Before you do anything else, unzip it:

- **Mac** — double-click the .zip file. A folder appears next to it.
- **Windows** — right-click the .zip file and choose **Extract All**, then click **Extract**.

The folder will be called something like **`python-music-workshop-main`**. Open it.

---

## Step 2 — Run the setup script

Open the **`setup`** folder inside the workshop folder.

### On a Mac

1. Find the file called **`setup.command`**
2. **Right-click** it and choose **Open**, then click **Open** again in the security prompt
3. A terminal window opens and runs the checks automatically

> If macOS still blocks it, let your volunteer know — they have a fix.

### On a Windows PC

1. Find the file called **`setup.bat`**
2. Double-click it
3. If Windows shows a blue "Windows protected your PC" screen, click **More info** then **Run anyway**
4. A command prompt window opens and runs the checks automatically

---

## Step 3 — Read the output

The script prints a result for each check:

```
[ OK ] Python 3.11.4
[ OK ] VS Code 1.89.0
[ OK ] Loaded 9237 songs.

*** ALL DONE — YOU'RE GOOD TO GO! ***
```

VS Code opens automatically when all three pass — skip to Step 4.

If something shows `[FAIL]`, you'll see exactly what to do:

```
[FAIL] Python — not found

  ISSUE 1: Python 3 is not installed.
  FIX 1:   Go to https://www.python.org/downloads/ and install Python 3.11.
```

Follow the **FIX** for each issue, then re-run the setup script. If you're stuck, show the window to your volunteer.

---

## Step 4 — Open your first exercise

Once VS Code is open:

1. In the left panel, click the **`exercises`** folder to expand it
2. Click **`exercise_01_variables_and_strings.py`**
3. Read through it — then start coding in the **YOUR TASK** section

To **run** the file, open a terminal in VS Code with `` Ctrl+` ``, then type:

```
python3 exercises/exercise_01_variables_and_strings.py
```

> On Windows, try `python` instead of `python3` if that doesn't work.

You should see output printed in the terminal. If you do — you're ready!

---

## Bonus — the Data Explorer

There's a webpage that lets you browse 9,000+ real songs and shows you how to access any of them in Python. Double-click **`explore.command`** (Mac) or **`explore.bat`** (Windows) from the `setup` folder to open it.

Press Enter in the terminal window (or close it) when you're done.

---

## Quick Reference

| Task | How |
|------|-----|
| Run setup checks | double-click `setup/setup.command` (Mac) or `setup/setup.bat` (Windows) |
| Run an exercise | `python3 exercises/exercise_01_variables_and_strings.py` in VS Code terminal |
| Open the data explorer | double-click `setup/explore.command` (Mac) or `setup/explore.bat` (Windows) |
