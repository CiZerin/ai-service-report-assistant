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

The project also includes an optional AI mode using Yandex AI Studio. If AI report generation fails, the program safely falls back to the manual report generator.

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
* Optional AI-generated report mode
* Yandex AI Studio integration through `ai_client.py`
* Safe manual fallback if AI report generation fails
* Local `.env` configuration for API credentials
* `.env.example` file with required environment variable names

## Current architecture direction

The project is being prepared for future backend, web interface, and Telegram bot support.

Current direction:

```text
Core report logic
↓
Interfaces:
- CLI now
- Web later
- Telegram later
```

The CLI is no longer responsible for all business logic. It now works mainly as an input interface, while report generation is handled by the service layer.

This makes the project easier to extend later with FastAPI, a web form, or a Telegram bot without duplicating report generation logic.



## Project structure

```text
ai-service-report-assistant/
├── main.py
├── report_service.py
├── priority.py
├── report_generator.py
├── structured_report.py
├── validator.py
├── ai_client.py
├── file_writer.py
├── interfaces/
│   ├── __init__.py
│   └── cli.py
├── storage/
│   ├── __init__.py
│   └── file_storage.py
├── examples/
│   ├── sample_notes.txt
│   ├── low_priority_case.txt
│   ├── medium_priority_case.txt
│   └── high_priority_case.txt
├── learning/
├── README.md
├── .env.example
└── .gitignore
```

The project is now split into simple layers:

```text
main.py
```

Program entry point.

```text
interfaces/cli.py
```

Terminal interface. It collects service case data from the engineer.

```text
report_service.py
```

Core report logic. It validates input, detects priority, uses AI mode if requested, keeps manual fallback, and creates both text and structured reports.

```text
storage/file_storage.py
```

Report saving logic. It creates timestamped `.txt` and `.json` report files.

```text
ai_client.py
```

Yandex AI Studio integration. If AI is unavailable or `.env` values are missing, the program safely falls back to manual report generation.



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

The program also asks whether to use AI-generated report mode:

```text
Use AI-generated report? yes/no:
```

If the user chooses `no`, the program creates the standard manual report.

If the user chooses `yes`, the program sends prepared service case notes to Yandex AI Studio and saves the AI-generated report as the `.txt` report.

If the AI request fails, the program shows a warning and creates a manual report instead:

```text
AI request failed. Manual report will be generated instead.
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

## AI mode with Yandex AI Studio

The project includes an optional AI-generated report mode using Yandex AI Studio.

AI logic is separated into:

```text
ai_client.py
```

The main AI function is:

```python
generate_ai_report(service_case_notes)
```

The main CLI program asks the user:

```text
Use AI-generated report? yes/no:
```

If the user chooses `no`, the program uses the standard manual report generator.

If the user chooses `yes`, the program prepares service case notes and sends them to Yandex AI Studio.

If the AI request fails, the program safely falls back to the manual report generator.

Current AI-related files:

* `.env` is used for real local API credentials and is excluded from Git.
* `.env.example` shows the required environment variables without real secrets.
* `ai_client.py` contains `generate_ai_report()`.
* `main.py` can use AI mode or manual mode.

Environment variables example:

```text
YANDEX_API_KEY=your_yandex_api_key_here
YANDEX_FOLDER_ID=your_yandex_folder_id_here
YANDEX_MODEL_URI=gpt://your_yandex_folder_id_here/yandexgpt-5.1/latest
```

Important: never commit the real `.env` file to GitHub.


## Next steps

Planned improvements for future versions:

* Show exactly which required fields are missing
* Improve AI error handling
* Read service case data directly from example files
* Add report creation date and time inside the report content
* Improve priority detection rules
* Add clearer terminal messages for manual mode and AI mode


