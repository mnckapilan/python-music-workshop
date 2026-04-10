# Volunteer Guide — Python Music Workshop

Quick reference for setup day. Students download a zip and run a setup script — your job is to unblock anything that fails.

---

## Before the session

1. Download the zip from GitHub and test the full setup flow on one laptop of each type (Mac + Windows)
2. Have this guide open on your phone or a spare laptop

---

## Distributing the files

Share the GitHub zip download link, or put the zip on a USB stick. Students unzip it themselves — remind them to **Extract All** on Windows, not just double-click and run from inside the zip.

The extracted folder will be called **`python-music-workshop-main`**.

---

## Mac setup

### Normal flow
1. Student opens `setup/setup.command` — right-click → Open → Open
2. Terminal runs checks, VS Code opens on success

### Mac issue: "setup.command cannot be opened because it is from an unidentified developer"
Even right-click → Open may fail on macOS Ventura/Sonoma for zip downloads. Fix the entire folder in one command:

```bash
xattr -rd com.apple.quarantine ~/Downloads/python-music-workshop-main
```

Adjust the path if they unzipped somewhere else. Run it in Terminal (Cmd+Space → Terminal). Then try `setup.command` again.

### Mac issue: smoke test fails (`[FAIL] Music data failed to load`)
Usually the same quarantine problem. Run the `xattr` command above, then re-run `setup.command`.

### Mac issue: VS Code installed but `code` command missing
The script detects this and gives the exact fix:
> Open VS Code → Cmd+Shift+P → type `shell command` → click **Shell Command: Install code command in PATH**

Then re-run `setup.command`.

---

## Windows setup

### Normal flow
1. Student double-clicks `setup/setup.bat`
2. If SmartScreen appears: click **More info** → **Run anyway**
3. Command prompt runs checks, VS Code opens on success

### Windows issue: SmartScreen blocks setup.bat
Click **More info** → **Run anyway**. If the student doesn't have admin rights, you may need to unblock it:

```powershell
Unblock-File -Path "C:\path\to\python-music-workshop-main\setup\setup.bat"
```

Or: right-click `setup.bat` → Properties → tick **Unblock** at the bottom → OK.

### Windows issue: smoke test fails (`[FAIL] Music data failed to load`)
Most likely the student ran `setup.bat` from inside the zip without extracting first. Make sure they right-clicked the zip → **Extract All** before running anything.

### Windows issue: Python found but wrong version
Student likely has Python 2 or an old Python 3 on the machine. Install Python 3.11 from python.org — tick **Add python.exe to PATH** on the first screen — then restart the command prompt and re-run `setup.bat`.

### Windows issue: VS Code installed but `code` command missing
The script detects this. Fix: uninstall VS Code and reinstall from code.visualstudio.com, ticking **Add to PATH** during installation. Restart the laptop, then re-run `setup.bat`.

---

## Port conflict (Data Explorer)

If a student gets `Port 8000 is already in use` when opening the explorer, they have another explorer window open. Close it (press Enter in that terminal or close the window), then try again.

---

## Quick diagnostics

| Symptom | Most likely cause | Fix |
|---------|-----------------|-----|
| Mac: script won't open at all | Quarantine on zip download | `xattr -rd com.apple.quarantine <folder>` |
| Mac: smoke test fails | Quarantine on data file | Same `xattr` command |
| Windows: blue SmartScreen screen | Internet zone flag on .bat | More info → Run anyway |
| Windows: smoke test fails | Ran from inside zip, not extracted | Extract All, then re-run |
| Either: Python not found | Not installed or not in PATH | Install Python 3.11, tick "Add to PATH" |
| Either: VS Code not found | Not installed or PATH missing | Install/reinstall VS Code, tick "Add to PATH" |
| Either: port 8000 in use | Explorer already open | Close the existing explorer window |
