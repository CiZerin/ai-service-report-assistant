service_tasks = [
    "Disk failed",
    "Firmware update failed",
    "Server doesn't start up",
    "Power supply failed",
    "Unknown warning message"
]

print("=== Service tasks ===")
print("Total tasks:", len(service_tasks))

high_priority_count = 0

for index, task in enumerate(service_tasks):
    task_lower = task.lower()

    if "firmware" in task_lower or "bbu" in task_lower or "power" in task_lower:
        priority = "HIGH"
        high_priority_count += 1
    elif "disk" in task_lower:
        priority = "NORMAL"
    else:
        priority = "CHECK REQUIRED"
    
    print(f"{index + 1}. {task} | Priority: {priority}")

print("High priority tasks:", high_priority_count)