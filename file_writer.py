import json

def save_report(filename, report):
    with open(filename, "w") as file:
        file.write(report)

def save_json_report(filename, report):
    with open(filename, "w") as file:
        json.dump(report, file, indent=4)