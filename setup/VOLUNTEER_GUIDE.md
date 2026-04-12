# Volunteer Guide — Python Music Workshop

Quick reference for the session. Students download a zip from GitHub, open the folder in Saarai, and run exercises from there.

---

## Before the session

1. Test the full flow yourself: download the zip, unzip it, open it in **saarai.dev**, run `exercise_00_setup_check.py`
2. Have the GitHub download link ready to share; Data Explorer is at **tinyurl.com/7tdxxp57**
3. Have this guide open on your phone or a spare laptop

---

## Distributing the files

Share **tinyurl.com/python-walthamstow-workshop**. Students click the green **Code** button → **Download ZIP**, then unzip it.

Remind Windows students to **right-click → Extract All** rather than opening files from inside the zip.

The extracted folder will be called something like **`python-music-workshop-main`**.

---

## Common issues

### Windows: files opened from inside the zip

**Symptom:** file not found errors, or the folder structure looks wrong in Saarai.

**Fix:** make sure the student right-clicked the zip → **Extract All** before opening anything. Files must be fully unzipped first.

---

### Saarai won't open the folder / browser asks for permission

**Mac:** the browser will ask for permission to access the local file system — click **Allow**.

**Windows:** same — click **Allow** or **Yes** when prompted.

---

### "File not found" errors when running exercises

The student likely opened a subfolder instead of the root workshop folder.

**Fix:** in Saarai, go to **File → Open Folder** and select the top-level `python-music-workshop-main` folder (not the `exercises` folder inside it).

---

### Run button does nothing / exercise won't run

Make sure the student has clicked a `.py` file in the left panel to open it in the editor before hitting Run.

---

## Quick diagnostics

| Symptom | Most likely cause | Fix |
|---------|-------------------|-----|
| File not found errors | Opened wrong folder in Saarai | File → Open Folder → select the root workshop folder |
| Songs won't load | Opened from inside zip | Extract All first, then re-open in Saarai |
| Mac: browser asks for file access | Normal permission prompt | Click Allow |
| Run button does nothing | No file open in editor | Click a `.py` file to open it first |
