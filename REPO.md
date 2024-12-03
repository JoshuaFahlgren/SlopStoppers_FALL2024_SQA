---
Team Name: Slop Stoppers
Team Members:
  - Joshua Fahlgren
  - Mathew Rogers
---

# Report

### Fuzzing

Fuzzing occurs in the fuzz.py file and targets the following methods:

1. MLForensics/mining/git.repo.miner.py makeChunks()
2. MLForensics/mining/mining.py dumpContentIntoFile()
3. MLForensics/FAME-ML/main.py getAllPythonFilesinRepo()
4. MLForensics/empirical/report.py Average()
5. MLForensics/empirical/report.py Median()

For each method, we generate 100 random inputs of the appropriate input-type and verify the exit status on execution.

### Forensics

Forensics logging occurs at the following locations in the MLForensics repo:

1. MLForensics/mining/log.op.miner.py getAllPythonFilesinRepo()
2. MLForensics/mining/mining.py dumpContentIntoFile()
3. MLForensics/FAME-ML/main.py getCSVData()
4. MLForensics/FAME-ML/main.py runFameML()
5. MLForensics/FAME-ML/main.py getAllPythonFilesinRepo()

These methods were chosen because they invoke with a significant amont of system calls, which are points of interest for malicious actors.

In order for many of the python files to be executed and to demonstrate the logging process, our team would need several files not provided. So, logging execution isn't provided here but the logging statements are simple enough to be sound.
