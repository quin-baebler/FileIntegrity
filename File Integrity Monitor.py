import hashlib
import os
import time

# Gives the user the option to create a new baseline or monitor files using an existing baseline
print("What would you like to do?")
print("A) Collect a new baseline")
print("B) Begin monitoring file with saved baseline")
response = input("Please select A or B: ").upper()
print("User selected - ", response)

# Calculates the hash of the file with SHA-25t6
def calculate_file_hash(filename):
    """Calculate the SHA-256 hash of a file"""
    with open(filename, "rb") as f:
        contents = f.read()
        file_hash = hashlib.sha256(contents).hexdigest()
        return file_hash
    
# Calculates the hashes of every file in the directory and compares them to the hashes previously stored
# Alerts the user if any new files were created or files were changed
def check_for_changes(hash_dict):
    """Check if any new file has been created or any file has changed"""
    current_dir = os.getcwd()
    child_items = os.listdir(current_dir)
    for item in child_items:
        if os.path.isdir(item):
            continue
        if os.path.isdir(item) or item == "baseline.txt":
            continue
        if item not in hash_dict:
            print(f"Alert! New file was created: {item}")
        else:
            file_hash = calculate_file_hash(item)
            if file_hash != hash_dict[item]:
                print(f"Alert! file has changed: {item}")

# Creates a new baseline file with the files in the current directory and their corresponding hashes
if response == "A":
    print("You selected 'A'. Collecting new baseline...")

    if os.path.exists("baseline.txt"):
    # if it exists, delete it
        os.remove("baseline.txt")
    # get the current working directory
    current_dir = os.getcwd()

    # get a list of the child items in the current directory
    child_items = os.listdir(current_dir)

    # print out the child items
    with open("baseline.txt", "w") as f:
    # iterate over the child items
        for item in child_items:
        # skip any directories in the list
            if os.path.isdir(item):
                continue
        # calculate the hash of the file
            hash_value = calculate_file_hash(item)
        # write the filename and hash value to the file
            f.write(item + ": " + hash_value + "\n")

        # print a message to indicate that the hash values have been written to the file
            print("Hash values written to baseline.txt")

# Using a baseline file checks the saved hashes compared to the current hashes to detect file changes
elif response == "B":
    print("You selected 'B'. Beginning monitoring file with saved baseline...")
    hash_dict = {}
    current_dir = os.getcwd()

    if os.path.exists("baseline.txt"):
        with open("baseline.txt", "r") as f:
            for line in f:
                # split the line into the path and hash values
                parts = line.strip().split(": ")
                # store the path and hash values in the dictionary
                hash_dict[parts[0]] = parts[1]
    else: print("No baseline found")

    # Infinte while loop that checks every 10 seconds to see if the files being monitored have changed
    while True:
        time.sleep(10)
        check_for_changes(hash_dict)
        


