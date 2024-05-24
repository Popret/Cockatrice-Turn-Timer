from datetime import datetime, timedelta
import re
from collections import defaultdict


log_pattern = re.compile(r"\[(.*?)\] (.*)'s turn\.")

total_time = defaultdict(timedelta)

parsed_logs = []

file_path = "time.txt"

with open(file_path, 'r') as file:
    log_lines = file.readlines()
    for line in log_lines:
        match = log_pattern.match(line.strip())
        if match:
            timestamp_str, player = match.groups()
            timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
            parsed_logs.append((timestamp, player))

for i in range(len(parsed_logs) - 1):
    start_time, player = parsed_logs[i]
    end_time, _ = parsed_logs[i + 1]
    if end_time < start_time:
        end_time += timedelta(days=1)  
    duration = end_time - start_time
    total_time[player] += duration

totalduration=0
for player, duration in total_time.items():
    print(f"{player}: {duration}")
    totalduration += duration

print(f"total duration: {totalduration}")

