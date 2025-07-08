import psutil
import json
import time

# Give the system a moment to breathe before measuring
time.sleep(1)

# First call to cpu_percent initializes the measurement
psutil.cpu_percent(interval=None)

# Now wait and get a fresh reading
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent

# Debug print to terminal
print(f"CPU: {cpu}% | RAM: {ram}%")

# Write to usage.json
with open("/home/mc/Desktop/htmltest/usage.json", "w") as f:
    json.dump({"cpu": cpu, "ram": ram}, f)

