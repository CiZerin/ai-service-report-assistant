# AI Service Report Assistant

A learning Python project for building a simple assistant for service engineers.

The project helps turn rough technical service notes into a structured service report.

## Project goal

The main goal is to build a practical tool that can:

* collect service case information;
* clean user input;
* detect fault priority;
* generate a structured service report;
* save the report to a `.txt` file.

In the future, this project will be prepared for AI API integration.

## Current features

* User input through the terminal
* Basic input cleaning with `.strip()`
* Fault priority detection
* Service report generation
* Report saving to `reports/service_report.txt`
* Organized project structure
* Git and GitHub version control

## Project structure

```text
ai-service-report-assistant/
├── main.py
├── priority.py
├── report_generator.py
├── file_writer.py
├── examples/
│   └── sample_notes.txt
├── reports/
│   └── service_report.txt
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

The generated report will be saved here:

```text
reports/service_report.txt
```

## Example output

```text
=== SERVICE REPORT ===
Engineer: Artem
Device: IBM DS3500
Serial: 78N6734
Issue: Power supply failed
Status: Check PSU status
Priority: HIGH
Action taken: Verified logs and PSU LED
Next step: Replace power supply
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

## Next steps

* Improve input validation
* Improve report file naming
* Add better error handling
* Prepare the project for future AI API integration
