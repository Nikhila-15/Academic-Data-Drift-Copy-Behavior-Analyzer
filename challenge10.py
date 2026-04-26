import random
import math
import copy
import numpy as np
import pandas as pd
roll_num = 2
limit = 5
records = []
for i in range(10):
    student = {
        "sid": i + 1,
        "marks": random.randint(40, 100),
        "attendance": random.randint(60, 100),
        "assignments": [random.randint(10, 30), random.randint(10, 30)]
    }
    records.append(student)
shallow_data = list(records)
deep_data = copy.deepcopy(records)
rule = roll_num % 3
for i in range(len(records)):
    if (rule == 0) or (i % rule == 0):
        shallow_data[i]["marks"] += int(math.sqrt(shallow_data[i]["marks"]))
        shallow_data[i]["assignments"][0] += 2
        shallow_data[i]["attendance"] -= 5
for i in range(len(records)):
    if (rule == 0) or (i % rule == 0):
        deep_data[i]["marks"] += int(math.sqrt(deep_data[i]["marks"]))
        deep_data[i]["assignments"][0] += 2
        deep_data[i]["attendance"] -= 5
df_original = pd.DataFrame(records)
df_shallow = pd.DataFrame(shallow_data)
df_deep = pd.DataFrame(deep_data)
avg_original = df_original["marks"].mean()
avg_deep = df_deep["marks"].mean()
std_dev = df_deep["marks"].std()
difference = abs(avg_original - avg_deep)
manual_avg = sum(df_deep["marks"]) / len(df_deep)
is_changed = not df_original.equals(df_shallow)
if is_changed:
    status = "Copy Failure Detected"
elif difference < 2:
    status = "Stable Data"
elif difference < limit:
    status = "Minor Drift"
else:
    status = "Critical Drift"
print("---- STUDENT DATA ANALYSIS ----\n")
print("Original Data:\n", df_original, "\n")
print("Shallow Copy:\n", df_shallow, "\n")
print("Deep Copy:\n", df_deep, "\n")
print("Original Mean:", avg_original)
print("Deep Mean:", avg_deep)
print("Standard Deviation:", std_dev)
print("Drift:", difference)
print("Tuple:", (avg_deep, difference, std_dev))
print("Manual Mean:", manual_avg)
print("Result:", status)