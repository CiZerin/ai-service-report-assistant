faults = [
    "BBU failed",
    "Disk failed",
    "Network adapter warning",
    "Power supply failed",
    "Firmware update failed",
    "Unknown hardware alert"
]

high_count = 0
normal_count = 0
check_required_count = 0

print("=== Fault counter ===")

for index, fault in enumerate(faults):
    fault_lower = fault.lower()

    if "firmware" in fault_lower or "bbu" in fault_lower or "power" in fault_lower:
        priority = "HIGH"
        high_count += 1
    elif "disk" in fault_lower:
        priority = "NORMAL"
        normal_count += 1
    else:
        priority = "CHECK REQUIRED"
        check_required_count += 1
    
    print(f"{index + 1}. {fault} -> {priority}")

print("----------------------")
print("Total faults:", len(faults))
print("High priority faults:", high_count)
print("Normal faults:", normal_count)
print("Check required faults:", check_required_count)