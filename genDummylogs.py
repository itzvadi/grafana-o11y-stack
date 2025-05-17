# save as log_writer.py
import time
from datetime import datetime
import os

log_file = "/var/log/dummy.log"

# Ensure the log file exists
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("Log initialized\n")

while True:
    with open(log_file, "a") as f:
        log_entry = f"{datetime.now().isoformat()} - Sample log data...\n"
        f.write(log_entry)
    time.sleep(2)  # every 2 seconds
