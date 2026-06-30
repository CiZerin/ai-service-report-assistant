# AI Service Report Assistant

A learning Python project for building a simple assistant for service engineers.

The project helps turn rough technical service notes into both a readable text report and a structured JSON report.

## Project goal

The main goal is to build a practical tool that can:

* collect service case information;
* clean user input;
* detect fault priority;
* generate a readable `.txt` service report;
* generate a structured Python dictionary;
* save the structured report to a `.json` file;
* validate required fields before creating reports.

In the future, this project will be prepared for AI API integration.

## Current features

* User input through the terminal
* Basic input cleaning with `.strip()`
* Required fields validation
* Fault priority detection
* Text service report generation
* Structured report generation as Python `dict`
* JSON report export
* Report saving to `reports/service_report.txt`
* JSON saving to `reports/service_report.json`
* Organized project structure
* Git and GitHub version control

## Project structure

```text
ai-service-report-assistant/
├── main.py
├── priority.py
├── report_generator.py
├── structured_report.py
├── file_writer.py
├── validator.py
├── examples/
│   └── sample_notes.txt
├── reports/
│   ├── service_report.txt
│   └── service_report.json
├── learning/
│   └── week_01/
├── README.md
└── .gitignore
```

## How to run

Open the project folder in the terminal and run:

```bash
python main.py
```

Then enter the requested service case information:

```text
Enter engineer name:
Enter device model:
Enter serial number:
Enter issue:
Enter current status:
Enter action taken:
Enter next step:
```

The generated reports will be saved here:

```text
reports/service_report.txt
reports/service_report.json
```

## Example text output

```text
=== SERVICE REPORT ===
Engineer: Artem
Device: Server
Serial: 11X2233
Issue: Disk failed
Status: Disk stop
Priority: NORMAL
Action taken: Logs checked
Next step: Replace disk
```

## Example JSON output

```json
{
    "engineer": "Artem",
    "device": "Server",
    "serial": "11X2233",
    "problem": "Disk failed",
    "symptoms": [
        "Disk failed"
    ],
    "status": "Disk stop",
    "priority": "NORMAL",
    "actions_taken": [
        "Logs checked"
    ],
    "recommended_next_steps": [
        "Replace disk"
    ],
    "customer_summary": "Server has issue: Disk failed. Current priority: NORMAL."
}
```

## Learning progress

### Week 1

* Python basics
* Variables and strings
* `if / elif / else`
* Lists
* Dictionaries
* Functions
* File writing
* Git and GitHub basics

### Week 2

* Project structure
* `main.py`
* Importing functions from other files
* User input with `input()`
* Input cleaning with `.strip()`
* Organizing folders
* Cleaner Git workflow

### Week 3

* Structured output
* Python dictionaries for report data
* Lists inside dictionaries
* JSON basics
* `json.dump()`
* Saving reports as `.json`
* Required fields validation
* Light refactoring of `main.py`
* Preparing the project for future AI API integration

## Next steps

* Improve report file naming
* Show exactly which required fields are missing
* Add better error handling
* Read input from example files
* Prepare for future AI API integration
