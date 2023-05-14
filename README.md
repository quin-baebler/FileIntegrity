# File Integrity Monitor


<h2>File Integrity Monitor</h2>
This is a simple file monitoring tool written in Python. It allows you to collect a baseline of files in a directory and then monitor those files for any changes.

<h2>How to use</h2>
When you run the tool, you will be prompted to either collect a new baseline or monitor files using an existing baseline.

<h2>Collect a new baseline</h2>
If you choose to collect a new baseline, the tool will calculate the SHA-256 hash for each file in the current directory and store them in a file called "baseline.txt". This file can be used as a baseline to compare against in the future.

<h2>Monitor files with saved baseline</h2>
If you choose to monitor files using an existing baseline, the tool will read the "baseline.txt" file and calculate the SHA-256 hash for each file in the current directory. If a file has changed, or a new file has been created since the baseline was collected, you will receive an alert.

The tool runs in an infinite while loop and checks for changes every 10 seconds.

<h2>Dependencies</h2>
This tool uses the following Python libraries:

- os
- time
- hashlib

<h2>Program Overview</h2>

The flow chart below gives a basic overview that was used to design the application.

<img width="514" alt="Screenshot 2023-05-13 at 11 21 45 PM" src="https://github.com/quin-baebler/FileIntegrityChecker/assets/91747413/29e7aa78-db7a-4070-8c59-9900d1712e5b">

Shoutout to <a href=https://www.youtube.com/@JoshMadakor>@JoshMadakor</a> for the project inspiration with his video on how to create a File Monitoring tool using Powershell.
