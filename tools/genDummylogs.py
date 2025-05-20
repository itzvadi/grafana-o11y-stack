import time
from datetime import datetime
import os

log_dir = "/logs"
log_file = os.path.join(log_dir, "dummy.log")

os.makedirs(log_dir, exist_ok=True)  # create folder if missing

# Create file if missing
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("Log initialized\n")

start_time = time.time()  # record start time
duration = 5 * 60  # 5 minutes in seconds

while True:
    current_time = time.time()
    if current_time - start_time > duration:
        print("Logging stopped after 5 minutes.")
        break  # stop logging after 5 minutes

    with open(log_file, "a") as f:
        f.write(f"{datetime.now().isoformat()} - itzvadi - Sample log data...\n")
    time.sleep(2)
