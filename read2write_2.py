import datetime
import pandas as pd

print("Input a name of a log file.")
with open(input(), "r") as f:
    lines = f.readlines()

start_info_pttrn = "Starting to analyze anomalies"
result_info_pttrn = "response anomaly results stored in DB."

success_start_infos = []
for line in lines:
    if start_info_pttrn in line:
        start_info = line
    elif result_info_pttrn in line:
        result_info = line
        try:
            success_start_infos.append(start_info)
        except NameError as e:
            print(e)

success_cases = pd.DataFrame()
for success_start_info in success_start_infos:
    for i in range(len(success_start_info)):
        if success_start_info[i] == "{":
            left = i + 1
        if success_start_info[i] == "}":
            right = i
    string = success_start_info[left:right]

    entries = []
    items = string.split(": ")
    for item in items:
        elements = item.split(" ")
        entry = " ".join(elements[:-1])
        entry = entry.strip(" ").strip(",").strip("'")
        if entry:
            entries.append(entry)
        entry = elements[-1]
        entry = entry.strip(" ").strip(",").strip("'")
        entries.append(entry)

    success_case = {}
    for i, entry in enumerate(entries):
        if i % 2 == 0:
            key = entry
        else:
            if entry.startswith("datetime"):
                value = eval(entry)
            else:
                value = entry
            success_case[key] = value
    success_cases = success_cases.append(success_case, ignore_index=True)

print("Input a name of a result file.")
success_cases.to_csv(input(), index=False)