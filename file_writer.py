import os
import json


def save_report(filename, report):
    os.makedirs("reports", exist_ok=True)

    with open(filename, "w") as file:
        file.write(report)

def save_json_report(filename, report):
    os.makedirs("reports", exist_ok=True)
    with open(filename, "w") as file:
        json.dump(report, file, indent=4)