# 🧹 Log File Cleaner (Python)

This Python script reads a log file and removes all lines that contain the word `DEBUG`. It then saves the cleaned version to a new file.

## ✅ What It Does

- Asks the user for a log file name
- Removes all `DEBUG` lines
- Saves the result in a new file (e.g. `cleaned_filename.txt`)
- Handles errors if the file doesn't exist or can't be read

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Save the script as `log_cleaner.py`.
3. In your terminal or command prompt, run:

```bash
python log_cleaner.py
Enter the name of the log file when asked.

📝 Example
Input (system.log):

[INFO] Start
[DEBUG] Something here
[ERROR] Oops!
Output (cleaned_system.log):

