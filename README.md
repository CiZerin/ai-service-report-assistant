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
* save the readable report to a `.txt` file;
* save the structured report to a `.json` file;
* create timestamped report filenames;
* validate required fields before creating reports.

In the future, this project will be prepared for AI API integration.

## Current MVP features

* User input through the terminal
* Basic input cleaning with `.strip()`
* Required fields validation
* Fault priority detection: `LOW`, `NORMAL`, `HIGH`, or `CHECK REQUIRED`
* Text service report generation
* Structured report generation as Python `dict`
* JSON report export
* Automatic `reports/` folder creation
* Timestamped report filenames
* Matching `.txt` and `.json` report names for each service case
* Example service cases for manual testing
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
├── ai_client.py
├── examples/
│   ├── sample_notes.txt
│   ├── low_priority_case.txt
│   ├── medium_priority_case.txt
│   └── high_priority_case.txt
├── learning/
│   ├── week_01/
│   └── week_05/
├── README.md
└── .gitignore
```

Generated reports are saved automatically in the `reports/` folder when the program runs.


## How to run

Open the project folder in the terminal and run:

```bash
python main.py
```

The program will ask for service case information:

```text
=== AI Service Report Assistant ===
Enter service case details below.

Enter engineer name:
Enter device model:
Enter serial number:
Enter issue:
Enter current status:
Enter action taken:
Enter next step:
```

After the report is created, the program shows where the files were saved:

```text
Report created successfully.
Text report saved to: reports/service_report_2026-07-01_09-52-13.txt
JSON report saved to: reports/service_report_2026-07-01_09-52-13.json
```

Each run creates a new pair of timestamped report files.


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

## Test service cases

The `examples/` folder contains simple manual test cases:

```text
examples/
├── low_priority_case.txt
├── medium_priority_case.txt
└── high_priority_case.txt
```

These files can be used to manually test priority detection:

* `low_priority_case.txt` — minor printer alignment issue, expected priority: `LOW`
* `medium_priority_case.txt` — degraded RAID array, expected priority: `NORMAL`
* `high_priority_case.txt` — device does not start, expected priority: `HIGH`

At this stage, the examples are used manually by copying the data into the terminal when running `python main.py`.


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

### Week 4

* First MVP version of the project
* Timestamped report filenames
* Matching `.txt` and `.json` report names for each service case
* Automatic `reports/` folder creation
* Improved CLI messages
* Clear final save paths in the terminal
* Manual test cases for `LOW`, `NORMAL`, and `HIGH` priority
* Improved priority detection rules
* Generated reports excluded from Git tracking
* README updated for GitHub portfolio presentation

## AI API preparation

In Week 5, the project was prepared for future AI API integration using Yandex AI Studio.

Current AI-related additions:

* `.env` is used for real local API credentials and is excluded from Git.
* `.env.example` shows the required environment variables without real secrets.
* `learning/week_05/` contains separate learning files for AI API experiments.
* `ai_client.py` contains a basic `generate_ai_report()` function.
* The current `main.py` CLI MVP still works without AI API.

Environment variables example:

```text
YANDEX_API_KEY=your_yandex_api_key_here
YANDEX_FOLDER_ID=your_yandex_folder_id_here
YANDEX_MODEL_URI=gpt://your_yandex_folder_id_here/yandexgpt-5.1/latest
```

## Next steps

Planned improvements for future versions:

* Show exactly which required fields are missing
* Add better error handling
* Read service case data directly from example files
* Add report creation date and time inside the report content
* Improve priority detection rules
* Prepare for future AI API integration

