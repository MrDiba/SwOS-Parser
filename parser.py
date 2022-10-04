#!/usr/bin/python3

# Translate SwitchOS wannabe JSON backup files to workable JSON and write it to a file.

import sys
import json
import re

# Check if there is an argument given.
if len(sys.argv) != 2:
    print("""
    Usage: python3 parser.py [FILE]
    When there is no FILE specified, print this information and quit

    Input: Backup from SwitchOS
    Output: JSON parsed backup from SwitchOS stored in FILE.json

    """)
    exit(1)

# Open the backup file and read its contents.
filename = str(sys.argv[1])
f = open(filename, "r")
contents = f.read()
f.close()

# Parse the SwitchOS data string so that it is readable for the JSON parser
contents = "{"+contents+"}" # Add {} to the outside of the string so it can be parsed using json.loads()
contents = re.sub('\'\'', '\"\"', contents) # Replace dual single quotes '' with "" for empty values
contents = re.sub('\'', '', contents) # Remove any single quotes around values
contents = re.sub('\.b', '', contents) # Remove the .b from the keys
contents = re.sub('\.', '', contents) # Remove the other dots
contents = re.sub('([\w.]+)', '"\g<1>"', contents) # Add dual quotes to the other values (words)
parsed_data = json.loads(contents)

# Write the parsed JSON data to a new file (or update an existing one)
f = open(filename+".json", "w")
f.write(json.dumps(parsed_data, indent=2))
f.close()
