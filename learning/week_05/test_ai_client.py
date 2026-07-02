import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from ai_client import generate_ai_report

notes = """
Engineer: Artem
Device: CT scanner
Serial: CT-7781
Issue: Intermittent gantry rotation error during scan preparation.
Status: Device works, but scan workflow is unstable.
Action taken: Checked error logs and inspected gantry drive system.
Next step: Schedule deeper mechanical inspection.
"""

report = generate_ai_report(notes)

print(report)