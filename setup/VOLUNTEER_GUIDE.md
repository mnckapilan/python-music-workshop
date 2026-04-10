# Volunteer Guide — Python Music Workshop

Quick reference for setup day. Students download a zip, run a setup script, and install VS Code — your job is to unblock anything that fails.

**Python is bundled** — students do not need Python installed on their machine. No Python troubleshooting needed.

---

## Before the session

1. Download the zip from **tinyurl.com/python-walthamstow-workshop** and test the full setup flow on one laptop of each type (Mac + Windows)
2. Have this guide open on your phone or a spare laptop

---

## Distributing the files

Share the link **tinyurl.com/python-walthamstow-workshop**, or put the zip on a USB stick. Students unzip it themselves — remind them to **Extract All** on Windows, not just double-click and run from inside the zip.

The extracted folder will be called **`python-music-workshop-main`**.

---

## Mac setup

### Normal flow

1. Student opens **Terminal** (Cmd+Space → *Terminal*)
2. Types `bash ` (with a space), drags **`setup/setup.command`** from Finder into Terminal, presses Enter
3. Script downloads the Python runtime if needed (~30 MB, one-time), then runs checks

### Mac issue: "cannot be opened because it is from an unidentified developer"

The setup script is run via `bash` directly, so Gatekeeper shouldn't block it. If you see this error on the runtime download, the script should clear quarantine automatically with `xattr`. If it still fails, run manually:

```bash
xattr -rd com.apple.quarantine ~/Desktop/python-music-workshop-main
```

Adjust the path if they unzipped somewhere else. Then re-run the setup.

### Mac issue: smoke test fails (`[FAIL] Music data failed to load`)

Usually a quarantine issue on the data file. Run the `xattr` command above, then re-run setup.

---

## Windows setup

### Normal flow

1. Student opens the `setup` folder in File Explorer
2. Clicks the **address bar** at the top → types `cmd` → presses Enter
3. Types `setup.bat` and presses Enter

### Windows issue: SmartScreen blocks setup.bat

Click **More info → Run anyway**. If the student doesn't have admin rights:

```powershell
Unblock-File -Path "C:\path\to\python-music-workshop-main\setup\setup.bat"
```

Or: right-click `setup.bat` → Properties → tick **Unblock** at the bottom → OK.

### Windows issue: smoke test fails (`[FAIL] Music data failed to load`)

Most likely the student ran `setup.bat` from inside the zip without extracting first. Make sure they right-clicked the zip → **Extract All** before running anything.

### Windows issue: Python runtime download fails

If the machine has no internet, copy the `python-runtime/` folder from a machine that has already run setup (or from a pre-prepared USB). Place it inside the workshop folder so the path is `python-music-workshop-main/python-runtime/windows/`.

---

## VS Code

VS Code is not checked by the setup script — it's a separate step students handle themselves (Step 3 in the slides). If a student doesn't have it: **code.visualstudio.com** → download and install.

If VS Code can't find `python3`, it may need to be pointed at the bundled runtime. The `python3` wrapper script (Mac) and `python3.bat` (Windows) in the project root handle this automatically when running from the VS Code terminal.

---

## Port conflict (Data Explorer)

If a student gets `Port 8000 is already in use` when opening the explorer, they have another explorer window open. Close it (press Enter in that terminal or close the window), then try again.

---

## Quick diagnostics

| Symptom | Most likely cause | Fix |
|---------|-------------------|-----|
| Mac: Gatekeeper blocks runtime | Quarantine on downloaded zip | `xattr -rd com.apple.quarantine <folder>` |
| Mac: smoke test fails | Quarantine on data file | Same `xattr` command |
| Windows: blue SmartScreen screen | Internet zone flag on .bat | More info → Run anyway |
| Windows: smoke test fails | Ran from inside zip, not extracted | Extract All, then re-run |
| Windows: runtime download fails | No internet / proxy | Copy `python-runtime/` folder from USB |
| Either: port 8000 in use | Explorer already open | Close the existing explorer window |
